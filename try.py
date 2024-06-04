from tools import ScrapeWebPage
import sys

website = "https://sameermahajan.wordpress.com"

if len(sys.argv) > 1:
    website = sys.argv[1]

print (ScrapeWebPage.get_content_with_URLs(website))