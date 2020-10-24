import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['uestc.edu.cn']
    # start_urls = ['https://news.uestc.edu.cn/']

    start_urls = [
        'https://news.uestc.edu.cn/?n = UestcNews.Front.Category.Page&CatId=42',
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
    ]

    def parse(self, response):
        #处理 start_urls的地址，并获得数据（剪切好数据）
        # ret1 = response.xpath("//div[id='Degas_news_list']").extract()

        # 该返回类型不是列表类型，是特殊列表类型
        li_list = response.xpath("//div[@id='Degas_wrap']//li").extract()
        # print(li_list)
        print(len(li_list))

        # for li in li_list:
        #     item ={}
        #       # 创建接收数据的字典，该字典包括title 和content两个属性
        #     item["title"] = li.xpath(".//h3/text()").extract_first()
        #     item["content"] = li.xpath(".//p/text()").extract_first()
        #     print(item)
            # print(len(li_list))
