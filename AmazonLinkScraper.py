import scrapy

class BookNamesSpider(scrapy.Spider):
    name = "mib_books_spider"
    base_url = 'https://ritholtz.com/page/'
    url_list = ["https://www.amazon.ca/winters-night-traveler-Italo-Calvino/dp/0156439611/ref=sr_1_1?crid=OFR3GSTM8QJ1&dchild=1&keywords=if+on+a+winters+night+a+traveller&qid=1603969872&sprefix=if+on+%2Caps%2C160&sr=8-1"]
    start_urls = url_list
    
    def parse(self, response):
        """ Main function that parses downloaded pages """
        # Print what the spider is doing
        ##print(response.url)
        # Get all the <a> tags
        ##a_selectors = response.xpath("//a")
        a_selectors = response.xpath("//ul/li[contains(., 'ISBN-10')]")
        
        
        
        
        for selector in a_selectors:
            spans = selector.xpath(".//span/text()[last()]")
            for span in spans: 
                elems = span.get().strip().replace('\n',"")
                if len(elems) == 10:
                
                    print("ISBN: "+'\t'+elems)
        