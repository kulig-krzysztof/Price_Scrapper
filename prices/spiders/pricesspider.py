import scrapy
from prices.items import PricesItem


class PricesspiderSpider(scrapy.Spider):
    name = 'pricesspider'
    allowed_domains = ['grailpoint.com']
    start_urls = [
        'http://grailpoint.com/cat-product/buty/?product-page=1',
        'http://grailpoint.com/cat-product/buty/?product-page=2',
        'http://grailpoint.com/cat-product/buty/?product-page=3',
        'http://grailpoint.com/cat-product/buty/?product-page=4',
        'http://grailpoint.com/cat-product/buty/?product-page=5',
        'http://grailpoint.com/cat-product/buty/?product-page=6',
        'http://grailpoint.com/cat-product/buty/?product-page=7',
        'http://grailpoint.com/cat-product/buty/?product-page=8',
        'http://grailpoint.com/cat-product/buty/?product-page=9',
        'http://grailpoint.com/cat-product/buty/?product-page=10',
        'http://grailpoint.com/cat-product/buty/?product-page=11',
        'http://grailpoint.com/cat-product/buty/?product-page=12',
        'http://grailpoint.com/cat-product/buty/?product-page=13',
        'http://grailpoint.com/cat-product/buty/?product-page=14',
        'http://grailpoint.com/cat-product/buty/?product-page=15',
        'http://grailpoint.com/cat-product/buty/?product-page=16'
        ]

    #custom_settings = {
    #    'FEEDS': { 'prices.csv': { 'format': 'csv', 'overwrite': True}}
    #}

    def parse(self, response):
        product_item = PricesItem()
        products =  response.css('a.woocommerce-LoopProduct-link.woocommerce-loop-product__link')
        for product in products:
            product_item['company'] =  product.css('div.label-group::text').get().replace('"', '').strip(),
            product_item['name'] = product.css('h3 > span::text').get(),
            product_item['price'] = product.css('span.woocommerce-Price-amount.amount > bdi::text').get().strip()
            yield product_item
        pass
