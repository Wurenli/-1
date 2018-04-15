#coding=utf-8
from __future__ import print_function
import csv
import os
import matplotlib.pyplot as plt

#比率标度属性
label_shuzhi=[
	'Number of Existing Stories',
	'Number of Proposed Stories',
	'Estimated Cost',
	'Revised Cost',
	'Existing Units',
	'Proposed Units',
	'Plansets'
]
filename='./hetu/'
with open('Building_Permits.csv') as cs:
	csv_reader=list(csv.reader(cs))
	labels=csv_reader[0]
	length=len(labels)
	leng=len(csv_reader)
	for i in range(length):
		#处理数值属性
		if labels[i] not in label_shuzhi:
			continue
		else:
			data=[]
			queshi_num=0
			for row in csv_reader[1:leng]:
				if row[i].strip()=='':
					queshi_num+=1
				else:
					data.append(float(row[i]))
			fig=plt.figure()
			ax=fig.add_subplot(111)
			ax.boxplot(data,sym='o',whis=0.05)
			
			plt.title(labels[i])
			plt.savefig(filename+labels[i]+'.png')
cs.close()