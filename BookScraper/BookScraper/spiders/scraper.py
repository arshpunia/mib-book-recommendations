import scrapy
from scrapy.loader import ItemLoader
from BookScraper.items import BookScraperItem

more_urls = []

    
class BrickSetSpider(scrapy.Spider):
    
    
    name = "episode_spider"
    base_url = 'https://ritholtz.com/category/podcast/mib/page/'
    url_list = []
    for i in range(2,8):
        page_url = base_url+str(i)+'/'
        url_list.append(page_url)
        
    start_urls = url_list
    
    def parse(self, response):
        """ Main function that parses downloaded pages """
        
        inner_main_selectors = response.xpath('//*[contains(@class,\'inner-main\')]')        
        for selector in inner_main_selectors:
            blog_posts = selector.xpath('//*[contains(@id,\'post\')]')
            for posts in blog_posts:
                post_id = posts.xpath("@id").extract_first()
                article_details = posts.xpath(".//header[@class=\"article-header\"]/a")
                for details in article_details:
                    text = details.xpath("@title").extract_first()
                # Extract the link href
                    link = details.xpath("@href").extract_first()
                    if "mib" in link:
                        ##print("+++"+str(link)+'\t'+str(text)+"\t"+str(post_id))
                        yield scrapy.Request(link, callback = self.parse_mib_link)
                        
                ##Taking that there are almost always two pages per podcast episode, but both of them point to the same #more fragment, we can simply scrape all the podcast episode pages and combine a list of only those pages that were referenced as containing the #more fragment. From there, we can compile the Amazon links and shakalakaboomboom. 
    

    
    def parse_mib_link(self, response):
        """ Main function that parses downloaded pages """
        inner_main_selectors = response.xpath('//*[contains(@class,\'inner-main\')]')        
        link_count = 0
        episode_notes_item = BookScraperItem()
        for selector in inner_main_selectors:
            blog_posts = selector.xpath('.//*[contains(@id,\'post-\')]')
            for posts in blog_posts:
                
                article_details = posts.xpath(".//a")
                for details in article_details:
                    
                
                    text = details.xpath("@title").extract_first()
                    link = details.xpath("@href").extract_first()
                    
                    
                    episode_notes_item['episode_notes_link'] = link
                    
                    
                    if "#more" in link:
                        yield {
                            'MoreLink': link
                        }
                        
                        ##print(dict(link = str(link_count)))
                        link_count+=1
                        """
                        with open('MoreLinks.txt','a') as m:
                            m.write(link+'\n')
                        """
        ##self.print_urls()
                ##Taking that there are almost always two pages per podcast episode, but both of them point to the same #more fragment, we can simply scrape all the podcast episode pages and combine a list of only those pages that were referenced as containing the #more fragment. From there, we can compile the Amazon links and shakalakaboomboom. 