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
	'Proposed Units']
label_tianchong=[
	'Number of Proposed Stories',
	'Number of Existing Stories',
	'Revised Cost',
	'Estimated Cost',
	'Proposed Units',
	'Existing Units']
filename='./zhifangtu/'
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
			tianchong=label_tianchong[label_shuzhi.index(labels[i])]
			tianchong_index=labels.index(tianchong)
			data=[]
			for row in csv_reader[1:leng]:
				if row[i].strip()=='':
					if row[tianchong_index].strip()!='':
						data.append(float(row[tianchong_index]))
				else:
					data.append(float(row[i]))
			fig=plt.figure()
			ax=fig.add_subplot(111)
			ax.hist(data,bins=20)
			plt.xlabel(labels[i])
			plt.ylabel('frequency')
			plt.title('histogram')
			plt.savefig(filename+labels[i]+'.png')
cs.close()