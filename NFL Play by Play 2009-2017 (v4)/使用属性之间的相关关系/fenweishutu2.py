#coding=utf-8
from __future__ import print_function
import csv
import os
import matplotlib.pyplot as plt


filename='./qq/'
with open('../NFL Play by Play 2009-2017 (v4).csv') as cs:
	csv_reader=list(csv.reader(cs))
	leng=len(csv_reader)

	x,y=[],[]
	for row in csv_reader[1:leng]:
		if row[70].strip()=='' or row[70]=='NA':
			if row[69].strip()!='' and row[69]!='NA':
				y.append(abs(float(row[69])))

		else:
			y.append(float(row[70]))
	y=sorted(y)
	l=len(y)
	for j in range(l):
		x.append(float(j+1-0.5)/float(l))
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(x,y)
	plt.xlabel("f")
	plt.ylabel('AbsScoreDiff')
	plt.title('q-q')
	plt.savefig(filename+'AbsScoreDiff.png')
cs.close()