#!/usr/bin/env python3

#For the case where we have the harmonized data already in CSV we randomly hash its id column.
import sys
import csv
import hashlib
import sha3
import argparse
from copy import copy
from random import *


def hash_id(str_id, method='sha3'):
    #  case where str_id is not a number
    try:
        random_num = float(str_id) + random()*100
        random_num_str = str(random_num).encode()
    except:
        random_num_str = str_id + str(random()*100)
        random_num_str = random_num_str.encode()
    if method == 'md5':
        random_hash_str = hashlib.md5(random_num_str)
    elif method == 'sha3':
        random_hash_str = sha3.sha3_224(random_num_str)
    # print("Row num:", str_id, "Random num: ", random_num_str, "Random Hash: ", random_hash_str.hexdigest())
    return random_hash_str.hexdigest()


def anonymize_csv(inputpath, outputpath, columns, method):
    print("We will anonymize file ", inputpath, " assuming its first column is its id.")
    lookup_id = {}
    csv_new = []
    with open(inputpath, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            new_row = copy(row)
            if line == 0:  # first row has the headers...
                csv_new.append(row)
                print("First row: Headers...")
            else:
                for column in columns:
                    lookup_id.setdefault(row[column], hash_id(row[column], method))
                    new_row[column] = lookup_id[row[column]]
                csv_new.append(new_row)
            line += 1
    with open(outputpath, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for row in csv_new:
            csv_writer.writerow(row)


def main():
    "CLI for anonymazation script"
    # Create a parser
    parser = argparse.ArgumentParser(description='Script for anonymization \
                                     of hospital EHR csv.')
    parser.add_argument('inputpath', type=str,
                        help='initial ehr csv to be anonymized')
    parser.add_argument('outputpath', type=str,
                        help='pathanonymized csv filepath')
    parser.add_argument('-m', '--method', choices=['md5', 'sha3'],
                        default='sha3', help='hash fucntion to be used')
    parser.add_argument('-c', '--columns', type=int, nargs='*', default=[1])
    args = parser.parse_args(sys.argv[1:])
    # substracting 1 to have python correct list indexes
    columns = [x - 1 for x in args.columns]
    # call the anonymiza function
    anonymize_csv(args.inputpath, args.outputpath, columns, args.method)

if __name__ == '__main__':
    main()
