# Wikipedia Web Crawler

Simple Python web crawler that automates "going down the rabbit hole" on Wikipedia.

The program starts with a random Wikipedia article, then repeatedly finds the first Wikipedia link in the body of the given Wikipedia url until one of three possibilities occur –– 

1) The pre-determined "target URL" is hit. In this case, the target URL is https://en.wikipedia.org/wiki/Language.
2) The pre-determined "maximum links" number is hit. In this case, this is specified to be 25 links.
3) The last link opened has already been opened as part of this exercise –– ergo, the program has hit a cycle.


This program was built as the final project for the Introduction to Python course on Udacity.
