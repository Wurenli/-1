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
filename='./qq/'
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
			x=[]
			y=[]
			queshi_num=0
			for row in csv_reader[1:leng]:
				if row[i].strip()=='':
					queshi_num+=1
				else:
					y.append(float(row[i]))
			y=sorted(y)
			l=len(y)
			for j in range(l):
				x.append((j+1-0.5)/float(l))
			fig=plt.figure()
			ax=fig.add_subplot(111)
			ax.scatter(x,y)
			plt.xlabel("f")
			plt.ylabel(labels[i])
			plt.title('q-q')
			plt.savefig(filename+labels[i]+'.png')
cs.close()