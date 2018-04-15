#coding=utf-8
from __future__ import print_function
import csv
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
# 比率标度属性
# label_shuzhi=[
# 	'Home_WP_pre',
# 	'Away_WP_pre',
# 	'Home_WP_post',
# 	'Away_WP_post']
# label_tianchong=[
# 	'Away_WP_pre',
# 	'Home_WP_pre',
# 	'Away_WP_post',
# 	'Home_WP_post']
# filename='./zhifangtu/'
# with open('../NFL Play by Play 2009-2017 (v4).csv') as cs:
# 	csv_reader=list(csv.reader(cs))
# 	labels=csv_reader[0]
# 	length=len(labels)
# 	leng=len(csv_reader)
# 	for i in range(length):
# 		#处理数值属性
# 		if labels[i] not in label_shuzhi:
# 			continue
# 		else:
# 			tianchong=label_tianchong[label_shuzhi.index(labels[i])]
# 			tianchong_index=labels.index(tianchong)
# 			data=[]
# 			for row in csv_reader[1:leng]:
# 				if row[i].strip()=='' or row[i]=='NA':
# 					if row[tianchong_index].strip()!='' and row[tianchong_index]!='NA':
# 						data.append(1-float(row[tianchong_index]))
# 				else:
# 					data.append(float(row[i]))
# 			fig=plt.figure()
# 			ax=fig.add_subplot(111)
# 			ax.hist(data,bins=20)
# 			plt.xlabel(labels[i])
# 			plt.ylabel('frequency')
# 			plt.title('histogram')
# 			plt.savefig(filename+labels[i]+'.png')
# cs.close()


filename='./zhifangtu/'
with open('../NFL Play by Play 2009-2017 (v4).csv') as cs:
	csv_reader=list(csv.reader(cs))
	leng = len(csv_reader)
	data=[]
	for row in csv_reader[1:leng]:
		if row[68].strip() == '' or row[68] == 'NA':
			if row[67].strip() != '' and row[67] != 'NA' and row[69].strip() != '' and row[69] != 'NA':
				data.append(float(row[67]) - float(row[69]))
		else:
			data.append(float(row[68]))
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.hist(data,bins=20)
	plt.xlabel('DefTeamScore')
	plt.ylabel('frequency')
	plt.title('histogram')   
	plt.savefig(filename+'DefTeamScore.png')
cs.close()

