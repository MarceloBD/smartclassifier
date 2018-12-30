import scrapy


class QuotesSpider(scrapy.Spider):
        name = "quotes"
    
        def start_requests(self):
            urls = [
                'https://www.magazineluiza.com.br/smartphone-samsung-galaxy-j8-64gb-preto-4g-4gb-ram-tela-6-cam-16mp-5mp-selfie-16mp/p/155540600/te/tcsp/',
                'https://www.magazineluiza.com.br/iphone-7-apple-128gb-preto-brilhante-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-10/p/218008400/te/teip/',
                'https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s9-128gb-preto-4g-cam-12mp-selfie-8mp-tela-5-8-quad-hd-octa-core/p/220282800/te/tcsp/',
                'https://www.magazineluiza.com.br/smartphone-qbex-joy-8gb-dual-chip-desbloqueado-cinza-/p/6366658/te/tcsp/'
            ]
            not_smart_urls = [
                    'https://www.magazineluiza.com.br/capa-para-celular-ultra-slim-galaxy-s8-5-8-vermelho-phone-case-/p/5139656/te/ccsm/',
                    'https://www.magazineluiza.com.br/capa-protetora-de-couro-para-iphone-7-plus-e-iphone-8-plus-apple/p/217070500/te/acci/',
                    'https://www.magazineluiza.com.br/capa-celular-spigen-galaxy-note-8-thin-fit-preta-587cs22051-/p/kf4851g6a7/te/ccsm/'
                    ]
            
            with open("train_data.tsv", "w") as record_file:  
                record_file.write("SOURCE	TITLE	CATEGORY\n")
            
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)
            
            for url in not_smart_urls:
                yield scrapy.Request(url=url, callback=self.parse_not_smart)
            
            
    
        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
            
            try: 
                title = response.css('h1.header-product__title::text').extract()[0]
            except:
                title = response.css('h1.header-product__title--unavailable::text').extract()[0]
                
            with open("train_data.tsv", "a") as record_file:  
                record_file.write(str(response.url)+"	"+str(title)+"	"+ str('smartphone')+"\n")
        
        def parse_not_smart(self, response):
            page = response.url.split("/")[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
            try: 
                title = response.css('h1.header-product__title::text').extract()[0]
            except:
                title = response.css('h1.header-product__title--unavailable::text').extract()[0]
            
            with open("train_data.tsv", "a") as record_file:  
                record_file.write(str(response.url)+"	"+str(title)+"	"+ str('nao-smartphone')+"\n")
        