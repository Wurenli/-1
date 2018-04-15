from __future__ import print_function
import csv
import os

label_shuzhi=[
	'Number of Existing Stories',
	'Number of Proposed Stories',
	'Estimated Cost',
	'Revised Cost',
	'Existing Units',
	'Proposed Units',
	'Plansets'
]
# filename='frequency.txt'
with open('Building_Permits.csv') as cs:
	# with open(filename,'w') as f:
		csv_reader=list(csv.reader(cs))
		labels=csv_reader[0]
		lenth=len(labels)
		leng=len(csv_reader)
		for i in range(lenth):
			result={}
			if labels[i] in label_shuzhi:
				for row in csv_reader[1:leng]:
					if not result.has_key(row[i]):
						result[row[i]]=0
					result[row[i]]+=1
				print('%s: %s,%d'%(labels[i],max(result),result[max(result)]))
cs.close()