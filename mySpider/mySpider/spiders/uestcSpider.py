import scrapy
from mySpider.items import MyspiderItem

class UestcSpider(scrapy.Spider):
    name = 'uestcSpider'
    allowed_domains = ['uestc.edu.cn']
    start_urls = [
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=42'
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=50',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=43',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=44',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=45',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=49',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=46',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=48',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=51',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=47',
        'https://news.uestc.edu.cn/?n=UestcNews.Front.Category.Page&CatId=15735'
    ]  # 爬取目标网页

    def parse(self, response):
        # 处理 start_urls的地址，并获得数据（剪切好数据）
        # ret1 = response.xpath("//div[id='Degas_news_list']").extract()

        # 该返回类型不是列表类型，是特殊列表类型
        url = response.xpath("//div[@id='Degas_news_list']//ul//li//h3")#获取每一页文章的URL，存储结构为列表
        # titles = response.xpath("//div[@id='Degas_news_list']//ul//li//h3//a/text()").extract()
        # contents = response.xpath("//div[@id='Degas_news_list']//ul//li//h3//a/@href").extract()
        # next_page = response.xpath("//div[@id='Degas_news_list']//div[@class='page_div']//ul[@class='pagination']//li[@class='move-page ']//a").extract()
        # item = MyspiderItem()
        # item = {}
        for list in url:#循环获取URL里面的
            # item['titles'] = list.xpath("//a/text()").extract()  # 获取标题
            article = list.xpath("a/@href").extract_first()
            article = response.urljoin(article)
            # item['contents'] = list.xpath("a/@href").extract() #获取内容网址
            # titles = list.xpath("//a/text()").extract()
            # contents = list.xpath("a/@href").extract()
            yield scrapy.Request(article, callback=self.parse_contents)

        next_page = response.xpath(
            "//ul[@class='pagination']//li[@class='move-page '][last()]//a/@href").extract_first()  # 获取下一页网址
        # print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_contents(self, response):
        item = MyspiderItem()
        title = response.xpath("//h1[@class='Degas_news_title']/text()").extract()
        content = response.xpath("//div[@class='Degas_news_content']//p/text()|//div[@class='Degas_news_content']//p//span/text()").extract()
        picture = response.xpath("//div[@class='Degas_news_content']//p//img/@src").extract()
        # picture = response.urljoin(picture)

        i = 0
        for p in picture:#将每一个url的相对地址改为绝对地址
            # print(picture[i])
            picture[i] = 'https://news.uestc.edu.cn' + p
            i = i+1

        item['title'] = title
        item['content'] = content
        item['picture'] = picture
        yield item
        #https://news.uestc.edu.cn/upload/image/name.jpg



