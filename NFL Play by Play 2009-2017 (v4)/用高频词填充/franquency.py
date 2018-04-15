from __future__ import print_function
import csv
import os

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
# filename='frequency.txt'
with open('../NFL Play by Play 2009-2017 (v4).csv') as cs:
	# with open(filename,'w') as f:
		csv_reader=list(csv.reader(cs))
		labels=csv_reader[0]
		lenth=len(labels)
		leng=len(csv_reader)
		for i in range(lenth):
			result={}
			if labels[i] in label_shuzhi:
				for row in csv_reader[1:leng]:
					if row[i]!='NA':
						if not result.has_key(row[i]):
							result[row[i]]=0
						result[row[i]]+=1
				print('%s: %f'%(labels[i],float(max(result))))
cs.close()