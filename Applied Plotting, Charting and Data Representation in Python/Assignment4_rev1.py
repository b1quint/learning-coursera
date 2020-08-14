
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[15]:

import pandas as pd
import matplotlib.pyplot as plt

CumulativeScores = pd.read_excel("National Women's Soccer League (NWSL).xlsx", sheetname='RegularSeasons2019')
Champions = pd.read_excel("National Women's Soccer League (NWSL).xlsx", sheetname='ChampionsBySeason')

CumulativeScores['WinPercentage'] = CumulativeScores['W']/( CumulativeScores['W'] + CumulativeScores['L'])
Top4Club = CumulativeScores.sort(columns='WinPercentage', ascending=False).reset_index(drop=True)
Top4Club = Top4Club.iloc[:4]['Club']


# In[17]:

ChampionsInfo = Champions.sort(columns='Season', ascending=False).reset_index(drop=True)
ChampionsInfo.rename(columns={'Runners-up_final':'2nd Place', 'Runners-up_season': '2nd in Shield'}, inplace=True)
#ChampionsInfo['Season ']=ChampionsInfo['Season']
ChampionsInfo.set_index('Season', inplace=True)
ChampionsInfo = ChampionsInfo.iloc[:4][['Champions', '2nd Place', 'Shield winners', '2nd in Shield']]


# In[18]:

Team_NCC = pd.read_excel("National Women's Soccer League (NWSL).xlsx", sheetname='NorthCarolinaCourage')
Team_PTFC= pd.read_excel("National Women's Soccer League (NWSL).xlsx", sheetname='PortlandThornsFC')
Team_CRS = pd.read_excel("National Women's Soccer League (NWSL).xlsx", sheetname='ChicagoRedStars')
Team_OLR= pd.read_excel("National Women's Soccer League (NWSL).xlsx", sheetname='OLRegion')
Team_PTFC = Team_PTFC[Team_PTFC['Season']!=2020].reset_index(drop=True)

Team_NCC['WinPercentage'] = Team_NCC['W']/( Team_NCC['W'] + Team_NCC['L'])
Team_PTFC['WinPercentage'] = Team_PTFC['W']/( Team_PTFC['W'] + Team_PTFC['L'])
Team_CRS['WinPercentage'] = Team_CRS['W']/( Team_CRS['W'] + Team_CRS['L'])
Team_OLR['WinPercentage'] = Team_OLR['W']/( Team_OLR['W'] + Team_OLR['L'])


# In[19]:

Team_NCC['Team'] = 'NorthCarolinaCourage'
Team_PTFC['Team'] = 'PortlandThornsFC'
Team_CRS['Team'] = 'ChicagoRedStars'
Team_OLR['Team'] = 'OLRegion'

NCC = Team_NCC[['Team','Season','Pts','WinPercentage']]
PTFC = Team_PTFC[['Team','Season','Pts','WinPercentage']]
CRS = Team_CRS[['Team','Season','Pts','WinPercentage']]
OLR = Team_OLR[['Team','Season','Pts','WinPercentage']]

All_Teams = pd.concat([NCC, CRS, PTFC, OLR])


# In[26]:

plt.figure()
Teams=pd.unique(All_Teams['Team'])
color=['darkred', 'red','g','lightgreen']
count=0
for i in Teams:
    Data = All_Teams[All_Teams['Team']==i]
    plt.plot(Data['Season'].tolist(), Data['WinPercentage'].tolist(), c=color[count], linewidth=2.4, alpha=0.7)
    count+=1
plt.xticks(pd.unique(All_Teams['Season']), alpha=0.9)
plt.xlabel('Season')
plt.ylabel('Winning Percentage %')
plt.title("Seasonal Performance of Top 4 Teams in National Women's Soccer League")
plt.legend(Teams, loc=(1.01, 0.05), frameon=False)
plt.figtext(1.26, 0.6, ChampionsInfo.iloc[:,:2], ha="left", fontsize=10, bbox={"boxstyle":'round', "facecolor":"lightblue", "alpha":0.5, "pad":1 })
plt.figtext(1.28, 0.2, ChampionsInfo.iloc[:,2:], ha="left", fontsize=10, bbox={"boxstyle":'round', "facecolor":"lightblue", "alpha":0.5, "pad":1 })
plt.figtext(1.06, 0.7, "Winning % = \n Win / (Win + Loss)", ha="center", fontsize=10, bbox={"boxstyle":'round', "facecolor":"lightgray", "alpha":0.5, "pad":1 })
plt.show()

