#coding=utf-8
from __future__ import print_function
import csv
import os
import matplotlib.pyplot as plt

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

label_tianchong=[9,999,98,9,99,9,99,9,90,71,9,9,9,9,9,3,3,3,3,3,0.001000,0.000994,0.001000,0.000983,
				 0.994605,
				 0.001000,
				 0.000997,
				 0.993128,
				 0.4735,
				 0.000990,
				 0.001000,
				 0.000990,
				 0.000100,
				 0.000999,
				 0.000001,
				 0.000999,
				 0.000001,
				 0.000001,
				 0.001000,
				 0.001000,
				 0.001000]

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
			data=[]
			freq=float(label_tianchong[label_shuzhi.index(labels[i])])
			for row in csv_reader[1:leng]:
				if row[i].strip()=='' or row[i]=='NA':
					data.append(freq)
				else:
					data.append(float(row[i]))
			fig=plt.figure()
			ax=fig.add_subplot(111)
			ax.boxplot(data,sym='o',whis=0.05)
			
			plt.title(labels[i])
			plt.savefig(filename+labels[i]+'.png')
cs.close()