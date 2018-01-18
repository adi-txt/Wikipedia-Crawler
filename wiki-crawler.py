import requests
import time
from bs4 import BeautifulSoup

# This function finds the first Wikipedia link in the body of a given Wikipedia url
def find_first_link(url):
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html, 'html.parser')
	
	content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

	article_link = None
	
	for element in content_div.find_all("p", recursive=False):
		if element.find("a", recursive=False):
			article_link = element.find("a", recursive=False).get('href')
			break

	if not article_link:
		return 
	
	first_link = 'https://en.wikipedia.org' + article_link
	return first_link

# This function checks if our Wikipedia crawler has hit the target url, crossed the max number of steps, or has hit a loop.
def continue_crawl(search_history, target_url, max_links = 25):
    if search_history[-1] == target_url:													
        print("\nWe've reached your specified target url - " + target_url[25:] + "\n")
        print("Wiki crawler ending...")
        print("Wiki crawler ended.\n")
        return False
    elif len(search_history) > max_links:
        print("\nOur search history has hit the 25 article barrier.\n")
        print("Wiki crawler ending...")
        print("Wiki crawler ended.\n")
        return False
    elif len(search_history) != len(set(search_history)):
        print("\nWe've hit a cycle.")
        print("The " + search_history[-1][30:] + " article is the article that repeats.\n")
        print("Wiki crawler ending...")
        print("Wiki crawler ended.\n")
        return False
    else:
        return True

# This is where the program begins running

start_url = "https://en.wikipedia.org/wiki/Special:Random" # leads to a random Wikipedia page
target_url = "https://en.wikipedia.org/wiki/Language"
article_chain = [start_url] # the list of articles crawled
article_count = 0 # the number of articles crawled.


print("\nYour start url is: " + start_url)
print("Your target url is: " + target_url)
print("\nWiki crawler starting...\n")

while continue_crawl(article_chain, target_url):

	print(str(article_count) + ": " + article_chain[-1])
	
	first_link = find_first_link(article_chain[-1])

	if not first_link:
		print("\nThe article has no links.\n")
		print("Wiki crawler ending...")
		print("Wiki crawler ended.\n")
		break
	
	article_chain.append(first_link) # add the first link found to article_chain
	
	article_count += 1 # increment the article count
	time.sleep(2) # delay for about two seconds

