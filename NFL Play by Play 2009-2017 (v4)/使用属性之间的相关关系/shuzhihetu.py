#coding=utf-8
from __future__ import print_function
import csv
import os
import matplotlib.pyplot as plt

#比率标度属性
label_shuzhi=[
	'Home_WP_pre',
	'Away_WP_pre',
	'Home_WP_post',
	'Away_WP_post']
label_tianchong=[
	'Away_WP_pre',
	'Home_WP_pre',
	'Away_WP_post',
	'Home_WP_post']
filename='./hetu/'
with open('../NFL Play by Play 2009-2017 (v4).csv') as cs:
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
				if row[i].strip()=='' or row[i]=='NA':
					if row[tianchong_index].strip()!='' and row[tianchong_index]!='NA':
						data.append(1-float(row[tianchong_index]))
				else:
					data.append(float(row[i]))
			fig=plt.figure()
			ax=fig.add_subplot(111)
			ax.boxplot(data,sym='o',whis=0.05)
			
			plt.title(labels[i])
			plt.savefig(filename+labels[i]+'.png')
cs.close()