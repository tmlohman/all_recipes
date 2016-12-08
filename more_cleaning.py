#!usr/bin/python

# check for and delete duplicate entries

import csv
'''
lastRow = None

with open('shortlines8.csv', 'w') as writefile:
	writer =  csv.writer(writefile, delimiter = '\t')

	
	with open('shortlines7.csv', 'r') as readfile:
		reader = csv.reader(readfile, delimiter = '\t')
		
		for line in readfile:
			data_mapped = line.strip().split('\t')
			
			# part 1
			
			# remove blank lines
			if len(data_mapped) == 1 and len(data_mapped[0]) == 0:
				continue
				
			# write good lines
			if len(data_mapped) == 11:
				writer.writerow(data_mapped)
				continue
			
			# check for first half of line, save to variable
			if len(data_mapped) == 9:
				data_mapped[-1] = data_mapped[-1].rstrip('\r\n')
				lastRow = data_mapped
				continue
				
			# if second half of line, concatenate with first half and write
			if lastRow != None:
				newRow = lastRow + data_mapped
				writer.writerow(newRow)
				lastRow = None
				print(newRow)
				print(" ")
				continue
				
			# else, just write the line
			
			writer.writerow(data_mapped)
			print(data_mapped)
			print(" ")
			
			# part 2
			# combine split descriptions
			if len(data_mapped) == 12:
				description = data_mapped[8] + data_mapped[9]
				data_mapped[8] = description
				del data_mapped[9]
				writer.writerow(data_mapped)
				print(data_mapped)
				print(len(data_mapped))
				print(" ")

				
			else:
				writer.writerow(data_mapped)
				print(data_mapped)
				print(len(data_mapped))
				print(" ")
				
			
			# part 3
			# check for first half of line, combine description, save to variable
			if len(data_mapped) == 10:
				description = data_mapped[8] + data_mapped[9]
				data_mapped[8] = description
				del data_mapped[9]
				data_mapped[-1] = data_mapped[-1].rstrip('\r\n')
				lastRow = data_mapped
				continue
				
			# if second half of line, concatenate with first half and write
			if lastRow != None:
				newRow = lastRow + data_mapped
				writer.writerow(newRow)
				lastRow = None
				print(newRow)
				print(len(newRow))
				print(" ")
				continue
				
			# else, just write the line
			writer.writerow(data_mapped)
			
			
			# part 4
			# combine split descriptions, repeat the process
			if len(data_mapped) == 12:
				description = data_mapped[8] + data_mapped[9]
				data_mapped[8] = description
				del data_mapped[9]
				writer.writerow(data_mapped)

				
			if len(data_mapped) == 10:
				description = data_mapped[8] + data_mapped[9]
				data_mapped[8] = description
				del data_mapped[9]
				data_mapped[-1] = data_mapped[-1].rstrip('\r\n')
				lastRow = data_mapped
				continue
				
			if lastRow != None:
				newRow = lastRow + data_mapped
				writer.writerow(newRow)
				lastRow = None
				continue
				
			# else, just write the line
			writer.writerow(data_mapped)
			if len(data_mapped) != 11:
				print(data_mapped)
				print(len(data_mapped))
				print(" ")
				
			
			# part 5
			# combine rows that got split after description
			if len(data_mapped) == 8:
				data_mapped[-1] = data_mapped[-1].rstrip('\r\n')
				lastRow = data_mapped
				continue
				
			if lastRow != None:
				newRow = lastRow + data_mapped
				writer.writerow(newRow)
				lastRow = None
				continue
				
			# else, just write the line
			writer.writerow(data_mapped)
			if len(data_mapped) != 11:
				print(data_mapped)
				print(len(data_mapped))
				print(" ")
				

			# part 6 
			# fix the stragglers
			if len(data_mapped) != 11:
				print(lastRow)
				print(len(lastRow))
				print(data_mapped)
				print(len(data_mapped))
				print(" ")
				
			lastRow = data_mapped
			
# part 7
# combine with full file
with open('data_cleaned.csv', 'w') as writefile:
	writer =  csv.writer(writefile, delimiter = '\t')

	
	with open('shortlines8.csv', 'r') as readfile:
		reader = csv.reader(readfile, delimiter = '\t')
		
		for line in readfile:
			data_mapped = line.strip().split('\t')
			
			if len(data_mapped) == 11:
				writer.writerow(data_mapped)
				
			else:
				print(data_mapped)
				
	with open('data_complete.csv', 'r') as readfile:
		reader = csv.reader(readfile, delimiter = '\t')
		
		for line in readfile:
			data_mapped = line.strip().split('\t')
			
			if len(data_mapped) == 11:
				writer.writerow(data_mapped)
				
			else:
				print(data_mapped)
			'''
# part 8
# replace "NA" values with "None"

with open('data_cleaned2.csv', 'w') as writefile:
	writer =  csv.writer(writefile, delimiter = '\t')

	
	with open('data_cleaned.csv', 'r') as readfile:
		reader = csv.reader(readfile, delimiter = '\t')
		
		for line in readfile:
			data_mapped = line.strip().split('\t')
			
			for i in range(0,10):
				if data_mapped[i] == "NA":
					data_mapped[i] = None
			
			writer.writerow(data_mapped)


