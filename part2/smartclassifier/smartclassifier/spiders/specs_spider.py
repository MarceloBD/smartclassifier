import scrapy
import re


class QuotesSpider(scrapy.Spider):
	name = "specs"
		
	def start_requests(self):
		urls = [
                'https://www.magazineluiza.com.br/smartphone-samsung-galaxy-j8-64gb-preto-4g-4gb-ram-tela-6-cam-16mp-5mp-selfie-16mp/p/155540600/te/tcsp/',
                'https://www.magazineluiza.com.br/iphone-7-apple-128gb-preto-brilhante-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-10/p/218008400/te/teip/',
                'https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s9-128gb-preto-4g-cam-12mp-selfie-8mp-tela-5-8-quad-hd-octa-core/p/220282800/te/tcsp/',
                'https://www.magazineluiza.com.br/smartphone-qbex-joy-8gb-dual-chip-desbloqueado-cinza-/p/6366658/te/tcsp/'
            ]
		with open("train_data.tsv", "w") as record_file:  
			record_file.write("SOURCE	TITLE	CATEGORY\n")
				
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
				
	def find_specifications(self, tags, response):
		for i in range(len(response.css('div.description table td::text').extract())):	
			title = response.css('div.description table td::text').extract()[i]
			
			for tag in tags:
				if (title.strip().lower() == tag.lower()):
					r = response.css('div.description table td::text').extract()[i+1].splitlines()
					for i in range(len(r)):
						r[i] = r[i].strip()
						r[i] = re.sub("[\(\[].*?[\)\]]", "", r[i])
					return ' '.join(r)
		return 'Indisponível'
				
	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
			self.log('Saved file %s' % filename)
			try: 
				title = response.css('h1.header-product__title::text').extract()[0]
			except:
				return 
            
			
			print('=============================Specs', self.find_specifications(['Marca'], response), self.find_specifications(['Memória RAM'], response), 
				 self.find_specifications(['Cor'], response), self.find_specifications(['Tamanho da Tela', 'Resolução', 'Resolução da tela'], response))