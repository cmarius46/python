from lxml import html
import requests

def clearSpaces(word):
	i = 0
	while (word[0].isalpha() or word[0].isalnum()) == False:
		word = word[1:]
		#print(word)
	return word

with open('search_word', 'r') as f:
	search_word = f.read()

with open('website_url', 'r') as f:
	url = f.read()

#url =  'https://carrefour.ro/catalogsearch/result/?q='#lapte

url = url + search_word

page = requests.get(url)

tree = html.fromstring(page.content)

with open('product_path') as f:
	product_path = f.read()

with open('price_path') as f:
	price_path = f.read()

products = tree.xpath(product_path) #'//a[@class="product-item-link"]/text()'

good_prices = tree.xpath(price_path) 
#'//span[@data-price-type="finalPrice"]/span/text()'


for i in range(len(products)):
	products[i] = clearSpaces(products[i])
	good_prices[i] = clearSpaces(good_prices[i])

with open('products', 'w') as f:
	for i in range(len(products)):
		#print('da')
		f.write(products[i])
		f.write('\n')

with open('prices', 'w') as f:
	for i in range(len(good_prices)):
		f.write(good_prices[i])
		f.write('\n')

