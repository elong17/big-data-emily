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