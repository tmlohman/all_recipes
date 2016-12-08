#!usr/bin/python

from lxml import html
import requests

index = range(256370, 256410)
good_index = []
bad_index = []

for i in index:
	get = 'http://allrecipes.com/recipe/' + str(i)
	
	try:
		page = requests.get(get)
		tree = html.fromstring(page.content)
		title = tree.xpath('//h1[@class="recipe-summary__h1"]/text()')[0]
		good_index.append(i)
		print(title + str(i))
	except:
		print("fail" + str(i))
		bad_index.append(i)

print (good_index)
print (len(good_index))	

	
