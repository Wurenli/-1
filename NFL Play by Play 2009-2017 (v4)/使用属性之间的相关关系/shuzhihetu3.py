#coding=utf-8
from __future__ import print_function
import csv
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
#比率标度属性

filename='./hetu/'
with open('../NFL Play by Play 2009-2017 (v4).csv') as cs:
	csv_reader=list(csv.reader(cs))
	leng=len(csv_reader)
	data=[]
	for row in csv_reader[1:leng]:
		if row[68].strip() == '' or row[68] == 'NA':
			if row[67].strip() != '' and row[67] != 'NA' and row[69].strip() != '' and row[69] != 'NA':
				data.append(float(row[67]) - float(row[69]))
		else:
			data.append(float(row[68]))
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.boxplot(data,sym='o',whis=0.05)

	plt.title('DefTeamScore')
	plt.savefig(filename+'DefTeamScore.png')
cs.close()