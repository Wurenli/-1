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
		if row[70].strip() == '' or row[70] == 'NA':
			if row[69].strip() != '' and row[69] != 'NA':
				data.append(abs(float(row[69])))

		else:
			data.append(float(row[70]))
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.boxplot(data,sym='o',whis=0.05)

	plt.title('AbsScoreDiff')
	plt.savefig(filename+'AbsScoreDiff.png')
cs.close()