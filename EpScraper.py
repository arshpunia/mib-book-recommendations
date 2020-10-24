import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    base_url = 'https://ritholtz.com/page/'
    url_list = []
    for i in range(1,101):
        page_url = base_url+str(i)+'/'
        url_list.append(page_url)
        
    ##start_urls = url_list
    start_urls = ["https://ritholtz.com/2020/05/mib-henry-cornell/","https://ritholtz.com/2020/05/mib-building-goldman-sachss-private-equity-business/"]
    
    
    def parse(self, response):
        """ Main function that parses downloaded pages """
        inner_main_selectors = response.xpath('//*[contains(@class,\'inner-main\')]')        
        for selector in inner_main_selectors:
            blog_posts = selector.xpath('.//*[contains(@id,\'post-\')]')
            for posts in blog_posts:
                
                article_details = posts.xpath(".//a")
                for details in article_details:
                    text = details.xpath("@title").extract_first()
                    link = details.xpath("@href").extract_first()
                    if "#more" in link:
                        print(str(link)+'\t'+str(text))
                    
                ##Taking that there are almost always two pages per podcast episode, but both of them point to the same #more fragment, we can simply scrape all the podcast episode pages and combine a list of only those pages that were referenced as containing the #more fragment. From there, we can compile the Amazon links and shakalakaboomboom. 
            
            