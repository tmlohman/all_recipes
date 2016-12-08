#!usr/bin/python

from lxml import html
import requests
import csv

with open('data11.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
	
	# write header to csv
	'''
	header = ['recipe_index', 'title', 'author', 'rating', 'rating_count', 
	'review_count', 'ready_in_time', 'calorie_count', 'description', 'ingredients', 
	'directions']
	writer.writerow(header)
	'''

	# pages to scrape from
	pages = range(134201, 140000)

	for p in pages:
		# make sure page is valid
		try:
			get = 'http://allrecipes.com/recipe/' + str(p)
			page = requests.get(get)
			tree = html.fromstring(page.content)
			title = tree.xpath('//h1[@class="recipe-summary__h1"]/text()')[0]
		except:
			print (str(p) + " failed")
			continue	
	
		# scrape data
		try:
			author = tree.xpath('//span[@class="submitter__name"]/text()')[0]
		except:
			author = "NA"
		try:
			rating = tree.xpath('//span[@class="aggregate-rating"]/meta/@*')[1]
		except:
			rating = "NA"
		try:
			rating_count = tree.xpath('//h4[@class="helpful-header"]/text()')[0].split()[0]
		except:
			rating_count = "NA"
		try:
			review_count = tree.xpath('//span[@class="aggregate-rating"]/meta/@*')[3]
		except:
			review_count = "NA"
		try:
			ready_in_time = tree.xpath('//span[@class="ready-in-time"]/text()')[0]
		except:
			ready_in_time = "NA"
		try:
			calorie_count = tree.xpath('//span[@class="calorie-count"]/span/text()')[0]
		except:
			calorie_count = "NA"
		try:
			description = tree.xpath('//div[@class="submitter__description"]/text()')[0]
		except:
			description = "NA"
		try:
			ingredients = tree.xpath('//span[@class="recipe-ingred_txt added"]/text()')
		except:
			ingredients = "NA"
		try:
			directions = tree.xpath('//span[@class="recipe-directions__list--item"]/text()')
		except:
			directions = "NA"
	    
	    # write data to csv
		data = [p, title, author, rating, rating_count, review_count, ready_in_time, calorie_count, description, ingredients, directions]
		
		print ("writing " + str(p))
		writer.writerow(data)
		

	



