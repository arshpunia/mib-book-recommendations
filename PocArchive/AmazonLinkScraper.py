import scrapy

class BookNamesSpider(scrapy.Spider):
    name = "mib_books_spider"
    url_list = []
    with open('AmazonLinks.txt','r') as f:
        amazon_links = f.readlines()
        for link in amazon_links:
            url_list.append(link.strip('\n'))
    url_list = ["https://www.amazon.com/exec/obidos/ASIN/B00OHXKIWG/thebigpictu09-20"]
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
                    
                    print(str(response)+'\t'+elems)
        