import scrapy
from scrapy_splash import SplashRequest
from fake_useragent import UserAgent
from scrapy.http.request import Request


class flipkartSpider(scrapy.Spider):
	name = "flipkart"
	retry_xpath = '//a[@class="_2cLu-l"]/@title'

	# def start_requests(self):
	# 	global keywords
	# 	yield scrapy.Request(url='https://www.flipkart.com/search?q=pringles%20sour%20cream%20and%20onion', callback = self.parse)

	def modify_realtime_request(self, request):
		# ua = UserAgent(fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
		request.headers["User-Agent"] =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
		request.meta['splash'] = False
		return request

	def parse(self, response):
		yield { 
        	"product": response.xpath('//a[@class="_2cLu-l"]/@title').extract(),
        	"price": response.xpath('//div[@class="_1vC4OE"]/text()').extract(),
        	"quantity": response.xpath('//div[@class="_1rcHFq"]/text()').extract(),
        	"url": response.xpath('//a[@class="_2cLu-l"]/@href').extract()
        	# "photourl": response.xpath('//div[@class="_3BTv9X"]//img/@src').extract()

        }
class naturesbasketSpider(scrapy.Spider):
	name = "naturesbasket"
	retry_xpath = '//a[@class="search_Ptitle"]/text()'

	# def start_requests(self):
	# 	global keywords
	# 	yield scrapy.Request(url='https://www.naturesbasket.co.in/Online-grocery-shopping/bourbon-biscuits?clk', callback = self.parse)

	def modify_realtime_request(self, request):
		# ua = UserAgent(fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
		request.headers["User-Agent"] =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
		return request

	def parse(self, response):

		# if "did not match any products" in response.xpath('//div[@class="EkstopViewmore"]/text()'):
		# 	yield {
		# 		"product": [],
		# 		"price": [],
		# 		"quantity": [],
		# 		"url": []
		# 	# "photourl": response.xpath('//div[@class="pro-buck-img"]//a//img/@src').extract()
		# }
		# else:
		yield {
			"product": response.xpath('//a[@class="search_Ptitle"]/text()').extract(),
			"price": response.xpath('//span[@class="search_PSellingP"]/text()').extract(),
			"quantity": response.xpath('//div[@class="search_PSelectedSize"]/text()').extract(),
			"url": response.xpath('//a[@class="search_Ptitle"]/@href').extract()
			# "photourl": response.xpath('//div[@class="pro-buck-img"]//a//img/@src').extract()
		}

class amazonSpider(scrapy.Spider):
	name = 'amazon'
	retry_xpath = '//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()'

	def modify_realtime_request(self, request):
		# ua = UserAgent(fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
		request.headers["User-Agent"] =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
		# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		request.meta['splash'] = True
		# request.meta['proxy'] = "http://104.144.1.199:3128"
		return request

# 	# def start_requests(self):
# 	# 	global keywords
# 	# 	yield scrapy.Request(callback = self.parse)
# 		# yield scrapy.Request(url='https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=cheetos', callback = self.parse)

	def parse(self, response):
		if response.xpath('//span[@class="a-price-whole"]/text()').extract():
			price = response.xpath('//span[@class="a-price-whole"]/text()').extract()
		else:
			price = response.xpath('//span[@class="a-color-price"]/text()').extract()

		yield {
			"product": response.xpath('//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()').extract(),
			"price": price,
			"url": response.xpath('//a[@class="a-link-normal a-text-normal"]/@href').extract()


			# "product": response.xpath('//div[@class="a-row a-spacing-none"]//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()').extract(),
	    	# "price": response.xpath('//div[@class="a-row a-spacing-none"]//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract(),
	    	# "location": response.xpath('//span[@id="glow-ingress-line2"]/text()').extract(),
	    	# "url": response.xpath('//div[@class="a-column a-span12 a-text-center"]//a[@class="a-link-normal a-text-normal"]/@href').extract()
	    	# "photourl": response.xpath('//a[@class="a-link-normal a-text-normal"]//img/@src').extract()
	    }


class grofersSpider(scrapy.Spider):
	name = 'grofers'        
	retry_xpath = '//div[@class="plp-product__name--box"]/text()'

# 	def start_requests(self):
# 		request = SplashRequest(url = 'https://grofers.com/s/?q=parle+g&suggestion_type=0&t=1', callback = self.parse, dont_filter=True)
# #        request.meta['proxy'] = 'https://' + self.proxy
# 		yield request

	def modify_realtime_request(self, request):
		request.meta['splash'] = True
		request.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
		return request

	def parse(self, response):
	
		yield {
			"product": response.xpath('//div[@class="plp-product__name--box"]/text()').extract(),
			"price": response.xpath('//span[@class="plp-product__price--new"]/text()').extract(),
			"quantity": response.xpath('//div[@class="plp-product__quantity"]/@title').extract(),
			"url": response.xpath('//a[@class="product__wrapper"]/@href').extract()
        	# "photourl": response.xpath('//img[@class="img-loader__img img-loader__img--shown img-loader__img--plp"]/@src').extract()
		}
            

