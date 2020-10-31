# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


class MyspiderPipeline:
    def process_item(self, item, spider):
        filename = 'UESTC_NEWS.txt'
        with open(filename,'a', encoding="utf-8") as f:
            f.write('title:   ')
            f.write(str(item['title'][0]))
            f.write('\n\n')
            f.write('picture_url:\n')
            for url in item['picture']:
                f.write(url)
                f.write('\n')
            f.write('\n')
            f.write('content:\n')
            for cont in item['content']:
                f.write(cont)
                f.write('\n')
            f.write('\n\n\n\n\n')

        return item
