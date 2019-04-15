#For the case where we have the harmonized data already in CSV we randomly hash its id column.
import sys
import csv
import hashlib
from copy import copy
from random import *

def hash_id(str_id):
	random_num = float(str_id) + random()*100
	random_num_str = str(random_num).encode()
	random_hash_str = hashlib.md5(random_num_str)
	print("Row num:", str_id, "Random num: ", random_num, "Random Hash: ", random_hash_str.hexdigest())
	return random_hash_str.hexdigest()


print("We will anonymize file ", sys.argv[1], " assuming its first column is its id.")
lookup_id = {}
csv_new = []
with open(sys.argv[1], mode='r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line=0
	for row in csv_reader:
		new_row = copy(row)
		if line==0: #first row has the headers...
			csv_new.append(row)
			print("First row: Headers...")		
		else:
			lookup_id.setdefault(row[0], hash_id(row[0]))
			new_row[0] = lookup_id[row[0]]
			csv_new.append(new_row)
		line += 1
with open(sys.argv[2], mode= 'w') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',')
	for row in csv_new:
		csv_writer.writerow(row)


    
