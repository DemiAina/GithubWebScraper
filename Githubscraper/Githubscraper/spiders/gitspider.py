import scrapy

class GitSpider(scrapy.Spider):
    name = 'Git'
    custom_settings = {'DOWNLOAD_DELAY': 10}
    start_urls = ['https://github.com/search?q=gaming']

    def parse(self, response):
        base_url = 'https://github.com'
        for gitlist in response.css("div.mt-n1.flex-auto"):
            try:
                yield{
                    'name': gitlist.css("a.v-align-middle::text").get(),
                    'RepoSummary':gitlist.css('p.mb-1::text').get().strip('\n'),
                    'Link': base_url + gitlist.css('a.v-align-middle').attrib['href'] ,
                }
            except:
                yield{

                    'name': gitlist.css("a.v-align-middle::text").get(),
                    'RepoSummary':'NULL',
                    'Link': base_url + gitlist.css('a.v-align-middle').attrib['href'] ,
                }
        next_page = base_url + response.css('a.next_page').attrib['href']
        if next_page is not base_url:
            yield response.follow(next_page, callback=self.parse)