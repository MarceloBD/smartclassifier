import scrapy

class QuotesSpider(scrapy.Spider):
        name = "quotes"
    
        def start_requests(self):
            urls = [
                'https://www.magazineluiza.com.br/smartphone-samsung-galaxy-j8-64gb-preto-4g-4gb-ram-tela-6-cam-16mp-5mp-selfie-16mp/p/155540600/te/tcsp/'
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)
    
        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
            
            with open("train_data.tsv", "w+") as record_file:  
                record_file.write("SOURCE	TITLE	CATEGORY\n")
                record_file.write(str(response.url)+"	"+str(response.css('h1.header-product__title::text').extract()[0])+"	"+ str('smartphone')+"\n")
        