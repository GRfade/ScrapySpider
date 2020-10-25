import scrapy


class UestcSpider(scrapy.Spider):
    name = 'uestcSpider'
    allowed_domains = ['uestc.edu.cn']
    # start_urls = ['https://news.uestc.edu.cn/']

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
        url = response.xpath("//div[@id='Degas_news_list']//ul//li//h3")
        # titles = response.xpath("//div[@id='Degas_news_list']//ul//li//h3//a/text()").extract()
        # contents = response.xpath("//div[@id='Degas_news_list']//ul//li//h3//a/@href").extract()
        # next_page = response.xpath("//div[@id='Degas_news_list']//div[@class='page_div']//ul[@class='pagination']//li[@class='move-page ']//a").extract()

        for list in url:
            # item['titles'] = list.xpath("//a/text()").extract()  # 获取标题
            # item['contents'] = list.xpath("a/@href").extract() #获取内容网址
            titles = list.xpath("//a/text()").extract()
            contents = list.xpath("a/@href").extract()
        print(2)
        next_page = response.xpath(
            "//ul[@class='pagination']//li[@class='move-page '][last()]//a/@href").extract_first()  # 获取下一页网址
        # print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

