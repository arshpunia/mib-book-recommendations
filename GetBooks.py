import scrapy

class BookNamesSpider(scrapy.Spider):
    name = "mib_books_spider"
    base_url = 'https://ritholtz.com/page/'
    url_list = []
    with open('BookList.txt','r') as f:
        episode_links = f.readlines()
        for link in episode_links:
            book_mentions = link.strip('\n')
            url_list.append(book_mentions)
    #url_list = ["https://ritholtz.com/2020/06/mib-jeremy-siegel-covid-market/#more-249305"]    
    start_urls = url_list
    
    def parse(self, response):
        """ Main function that parses downloaded pages """
        # Print what the spider is doing
        ##print(response.url)
        # Get all the <a> tags
        ##a_selectors = response.xpath("//a")
        a_selectors = response.xpath("//a[contains(@href, 'amazon')]")
        # Loop on each tag
        #a_selectors = response.xpath('//header[@class="article-header"]/a')
        with open('AmazonLinks.txt','a') as f:
            for selector in a_selectors:
                text = selector.xpath("text()").extract_first()
                    # Extract the link href
                link = selector.xpath("@href").extract_first()
                ##print(str(selector))
                
                    
                if "amazon" in link:
                    if not (text is None):
                        f.write(link+'\n')
            