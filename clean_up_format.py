#!usr/bin/python

# combine files and clean up csv formatting

import csv


file_list_1 = ['1a.csv', '2a.csv', '3a.csv', '4a.csv', '5a.csv', '6a.csv', '7a.csv']
file_list_2 = ['1b.csv', '2b.csv', '3b.csv', '4b.csv', '5b.csv', '6b.csv', '7b.csv']

c = 0
descriptions = []
with open('data_complete.csv', 'w') as writefile:
	
	for i in range(0,6):	
		with open(file_list_2[i], 'r') as file2:
			reader2 = csv.reader(file2, delimiter = '\t')
	
			for line in reader2:
				index = line[0]
				description = line[1][1:-2]
				descriptions.append([index, description])
				
		
		with open(file_list_1[i], 'r') as file1:
			reader1 = csv.reader(file1, delimiter = '\t')
			writer = csv.writer(writefile, delimiter = '\t')
			
			for line in reader1:
				data_mapped = line
	
	
				index = data_mapped[0]
				title = data_mapped[1]
				author = data_mapped[2]
				rating = data_mapped[3]
				rating_count = data_mapped[4]
				review_count = data_mapped[5]
				ready_in_time = data_mapped[6]
				calorie_count = data_mapped[7]
				ingredients = data_mapped[9]
				directions = data_mapped[10]
	
				
				if descriptions[c][0] == index:
					description = descriptions[c][1]
					
	
					row = [index, title, author, 
					rating, rating_count, review_count, 
					ready_in_time, calorie_count, 
					description, ingredients, directions]
					writer.writerow(row)
					
					
				else:
					print(descriptions[c])
					print(index)
					
				c += 1
	
	
	
	
	
