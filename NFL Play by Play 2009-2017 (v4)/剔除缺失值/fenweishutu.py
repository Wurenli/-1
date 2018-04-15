#coding=utf-8
from __future__ import print_function
import csv
import os
import matplotlib.pyplot as plt

#比率标度属性
label_shuzhi=[
	'TimeUnder',
	'TimeSecs',
	'PlayTimeDiff',
	'yrdln',
	'yrdline100',
	'ydstogo',
	'ydsnet',
	'AirYards',
	'YardsAfterCatch',
	'FieldGoalDistance',
	'Penalty.Yards',
	'PosTeamScore',
	'DefTeamScore',
	'ScoreDiff',
	'AbsScoreDiff',
	'posteam_timeouts_pre',
	'HomeTimeouts_Remaining_Pre',
	'AwayTimeouts_Remaining_Pre',
	'HomeTimeouts_Remaining_Post',
	'AwayTimeouts_Remaining_Post',
	'No_Score_Prob',
	'Opp_Field_Goal_Prob',
	'Opp_Safety_Prob',
	'Opp_Touchdown_Prob',
	'Field_Goal_Prob',
	'Safety_Prob',
	'Touchdown_Prob',
	'ExPoint_Prob',
	'TwoPoint_Prob',
	'ExpPts',
	'EPA',
	'airEPA',
	'yacEPA',
	'Home_WP_pre',
	'Away_WP_pre',
	'Home_WP_post',
	'Away_WP_post',
	'Win_Prob',
	'WPA',
	'airWPA',
	'yacWPA'
]
filename='./qq/'
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
			x=[]
			y=[]
			queshi_num=0
			for row in csv_reader[1:leng]:
				if row[i].strip()=='' or row[i]=='NA':
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