from __future__ import print_function
import csv
import os

filename='./biaocheng/'
with open('Building_Permits.csv') as cs:
	csv_reader=list(csv.reader(cs))
	labels=csv_reader[0]
	lenth=len(labels)
	l=len(csv_reader)
	for i in range(lenth):
		filename1=filename+labels[i]+'.txt'
		result={}

		for row in csv_reader[1:l]:
			if not result.has_key(row[i]):
				result[row[i]]=0
			result[row[i]]+=1
		keys=result.keys()
		with open(filename1,'w') as f:
			for key in keys:
				f.write("%s:%d\n"%(key,result[key]))
		f.close()
cs.close()