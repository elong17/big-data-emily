# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:59:20 2017

@author: elong
"""

df.Contest.unique()

df_turnout=df.loc[df['Contest']=='VOTER TURNOUT - TOTAL']
df_turnout.head()

min_turnout = df_turnout.loc[df['PctCnt']==df_turnout['PctCnt'].min()]
max_turnout = df_turnout.loc[df['PctCnt']==df_turnout['PctCnt'].max()]

df_turnout_tot = df.loc[df['Contest']=='BALLOTS CAST - TOTAL']



HW
grouped = df_voters.groupby('12') # Group by party registrations
summed = grouped['12'].count() # Get counts of each group
summed.sort_values(inplace=True, ascending=False)
df_summed = summed.to_frame()
df_summed.columns = ['NUMBER']
df_summed.index.names = ['PARTY']
df_summed

df_summed[(df_summed.index != 'D') & (df_summed.index != 'R')]

parties = ['Democrat', 'Republican', 'Other']
values = np.array([df_summed[(df_summed.index == 'D')].NUMBER.item(),df_summed[(df_summed.index == 'R')].NUMBER.item(),df_summed[(df_summed.index != 'D') & (df_summed.index != 'R')].NUMBER.sum()])
df_parties = pd.DataFrame(values,index=parties,columns=list('N'))
df_parties             
