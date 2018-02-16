'''Mailing List CSV File Reader

Open csv file and return mailing list'''

import csv

data = open("/Users/ChaewonKong/Desktop/pyWeb/pyProjects/mailing.csv", 'r', encoding="UTF-8")
# csvReader = csv.reader(data)
dictreader = csv.DictReader(data)

# print(dictreader.fieldnames)

for row in dictreader: #csvReader:
	print(row["E-mail"])
	