#coding=utf-8
from __future__ import print_function
import csv
import os
import matplotlib.pyplot as plt

#比率标度属性

filename='./hetu/'
with open('../NFL Play by Play 2009-2017 (v4).csv') as cs:
	csv_reader=list(csv.reader(cs))
	leng=len(csv_reader)
	data=[]
	for row in csv_reader[1:leng]:
		if row[-3].strip()=='' or row[-3]=='NA':
			if row[-4].strip()!='' and row[-4]!='NA' and row[-2].strip()!='' and row[-2]!='NA':
				data.append(float(row[-4]) - float(row[-2]))
		else:
			data.append(float(row[-3]))
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.boxplot(data,sym='o',whis=0.05)

	plt.title('airWPA')
	plt.savefig(filename+'airWPA.png')
cs.close()