#https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

import requests
from bs4 import BeautifulSoup
import csv

url1 = 'https://web.archive.org/web/20121007172955'
url2 = '/https://www.nga.gov/collection/anZ'
url3 = '1'
url4 = '.htm'

url = url1 + url2 + url3 + url4

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

last_links = soup.find(class_ = 'AlphaNav')
last_links.decompose()

names_list = soup.find(class_='BodyText')

names = names_list.find_all('a')

for name in names:
	actual_name = name.contents[0]
	link = 'https://web.archive.org' + name.get('href')
	print(actual_name, end = '\n')
	print(link, end = '\n\n')
	f.writerow([actual_name, link])


pages = []
for i in range(1, 5):
	url = url1 + url2 + str(i) + url4
	pages.append(url)

for item in pages:
	page = requests.get(item)
	soup = BeautifulSoup(page.text, 'html.parser')

	last_links = soup.find(class_='AlphaNav')
	last_links.decompose()

	artist_name_list = soup.find(class_='BodyText')
	artist_name_list_items = artist_name_list.find_all('a')

	for artist_name in artist_name_list_items:
		names = artist_name.contents[0]
		link = 'https://web.archive.org' + artist_name.get('href')

		f.writerow([names, link])