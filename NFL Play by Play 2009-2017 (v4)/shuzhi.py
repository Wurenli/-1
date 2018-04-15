#coding=utf-8
from __future__ import print_function
import csv
import os
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

filename='shuzhi.txt'
with open('./NFL Play by Play 2009-2017 (v4).csv') as cs:
	with open(filename,'w') as f:
		csv_reader=list(csv.reader(cs))
		labels=csv_reader[0]
		lenth=len(labels)
		
		for i in range(lenth):                                         
				#处理数值属性
				if labels[i] in label_shuzhi:
					data=[]
					queshi_num=0
					for row in csv_reader:
						if row[i]==labels[i]:
							continue
						elif row[i].strip()=='' or row[i]=='NA':
							queshi_num+=1
						else:
							data.append(float(row[i]))

				else:
					continue
				f.write("%s:\n"%labels[i])
				if len(data)>0:
					len1=len(data)
					sorted_data=sorted(data)
					max_mum=max(data)#最大值
					min_mum=min(data)#最小值
					mid_mum=sum(data)/float(len1)#均值
					mid_num=sorted_data[len1/2]#中位数
					quater_1=sorted_data[len1/4]#四分为数
					quater_3=sorted_data[len1-len1/4]#四分位数		
				
					f.write("最大值:%.2f 最小值:%.2f 均值:%.2f 中位数:%.2f 四分位数_1:%.2f 四分位数_3:%.2f 缺失值:%d\n"%(max_mum,min_mum,min_mum,mid_num,quater_1,quater_3,queshi_num))
	f.close()
cs.close()