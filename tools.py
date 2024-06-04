from bs4 import BeautifulSoup, NavigableString, Tag
from langchain.tools import tool
import requests
from urllib.parse import urljoin

class MyBeautifulSoup(BeautifulSoup):
    def _all_strings_plus(  self, strip=True, types=NavigableString, 
                            aRef={'a': lambda a: f"<{a.get('href', '')}>"}, 
                            skipTags=['script', 'style']    ):
        # verify types
        if hasattr(types,'__iter__') and not isinstance(types,type):
            types = tuple([t for t in types if isinstance(t, type)])
        if not (types and isinstance(types,(type,tuple))): 
            types = NavigableString
        
        # skip text in tags included in aRef
        # skipTags += list(aRef.keys())
        
        for descendant in self.descendants:
            # yield extra strings according to aRef
            if isinstance(descendant, Tag) and descendant.name in aRef:
                extraStr = aRef[descendant.name](descendant)
                if isinstance(extraStr, str): yield extraStr

            # skip text nodes DIRECTLY inside a Tag in aRef
            # if descendant.parent.name in aRef: continue

            # skip ALL text nodes inside skipTags 
            if skipTags and descendant.find_parent(skipTags): continue

            # default behavior
            if not isinstance(descendant, types): continue

            if strip:
                descendant = descendant.strip()
                if len(descendant) == 0: continue
            yield descendant

    def get_text_plus(self, separator=" ", srcUrl=None, **aspArgs):
        if srcUrl and isinstance(srcUrl, str):
            def hrefStr(aTag):
                href = aTag.get('href')
                if not (href is None or href.startswith('javascript:')):
                    return f"<{urljoin(srcUrl, href)}>"
            aspArgs.setdefault('aRef', {})
            aspArgs['aRef']['a'] = hrefStr
        
        return separator.join(self._all_strings_plus(**aspArgs))
    

class ScrapeWebPage:

    @tool("Read webpage content")
    def get_content(website: str) -> str:
        """Read content from a webpage"""
        soup = BeautifulSoup(requests.get(website).content, 'html.parser')
        all_content = "link: " + website + "\n" + \
                    "content: " + soup.body.get_text().strip()
        return all_content

    @tool("Read webpage content with URLs")
    def get_content_with_URLs(website: str) -> str:
        """Read content from a webpage. Include URLs on the page."""
        print ("website = ", website)
        response = requests.get(website)
        # print ("response = ", response)
        # print ("response.content = ", response.content)
        soup = MyBeautifulSoup(response.content, 'html.parser')
        # print ("soup.body = ", soup.body)
        # print ("type(soup.body) = ", type(soup.body))
        all_content = "link: " + website + "\n" + \
                    "content: " + soup.get_text_plus()
        return all_content
    
    def get_content_from_pages(website, pages, include_URLs = False):
        if include_URLs:
            soup = MyBeautifulSoup(requests.get(website).content, 
                                                   'html.parser')
            all_content = "link: " + website + "\n" + "content: " + \
                                soup.get_text_plus().strip()
        else:
            soup = BeautifulSoup(requests.get(website).content, 'html.parser')

            all_content = "link: " + website + "\n" + \
                    "content: " + soup.body.get_text().strip()

        scraped = set(website)
        pages = soup.find_all('a')

        for page in pages:
            if page.has_attr('href'):
                link = page['href']
                if not scraped.__contains__(link):
                    try:
                        if include_URLs:
                            soup = MyBeautifulSoup(requests.get(link).content, 
                                                   'html.parser')
                            current_content = "#######\n" + \
                                    "link: " + link + "\n" + "content: " + \
                                    soup.get_text_plus().strip() + \
                                    "#######\n"
                        else:
                            soup = BeautifulSoup(requests.get(link).content, 
                                                'html.parser')
                            current_content = "#######\n" + \
                                    "link: " + link + "\n" + "content: " + \
                                    soup.body.get_text().strip() + \
                                    "#######\n"
                        all_content += current_content
                    except:
                        # ignore exceptions like MissingSchema
                        pass
                    scraped.add(link)

        return all_content
    
    @tool("Read webpage content")
    def get_all_content(website: str) -> str:
        """Read content from a webpage and all the URLs in it."""
        return ScrapeWebPage.get_content_from_pages(website)
    
    @tool("Read webpage content with URLs")
    def get_all_content_with_URLs(website: str) -> str:
        """Read content from a webpage all the URLs in it. The content should
        also contain the embedded URLs on these pages."""
        return ScrapeWebPage.get_content_from_pages(website, True)
