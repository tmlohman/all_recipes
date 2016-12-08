#!usr/bin/python

import csv

files = ['data.csv', 'data11.csv', 'data12.csv', 'data2.csv', 
'data3.csv', 'data31.csv', 'data32.csv']

with open('data_complete', 'w') as writefile:
	
	for f in files:
		
		with open(f, 'r') as readfile:
			
			reader = csv.reader(readfile)
			
			for line in reader:
				
				print (line[0])
				break
