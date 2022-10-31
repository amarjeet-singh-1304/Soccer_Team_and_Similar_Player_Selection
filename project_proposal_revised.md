#### SER594: Revised Project Proposal
#### Soccer team and similar player Selection(title)
#### Amarjeet Singh (author)
#### 30 October 2022 (date)

Keywords:  Soccer Team Selection, Player Skills Analysis, Sports Analytics

Description: 
As we know that statistical and predictive analytics has got the attention among all the industries to help the 
stakeholders to plan their business. At the same time, many sports companies are also using it 
to understand the different patterns (like goal scoring pattern of a player) and helping the 
owners to plan their club business accordingly. In this project, I will be working on the soccer
attributes(skills) data related to different players across the world (mostly from European 
leagues). In the generated dataset, attributes have been rated based on player’s performance in 
the range of 0-100.In this project, I will be focussing on creating
a team based on the cost and findings similar players based on different attributes. Also, the model will be trained
to predict the overall ratings based on player's different attributes values.The data will 
be of quantitative type mostly discrete data. All analysis and visualization will be done using Python libraries.

There are multiple questions that can be asked but few are mentioned below:
1.	Which club team is the most valuable in the Europe?
2.	Best young players for each position?
3.	How different soccer skills are correlated to each other for players of different positions?
4.	Which player is best fit to play at a particular position in case of any injury to first 
    team player?
5.	Comparing different countries/leagues based on different attributes.

Research Questions:
1)
RO1 : To describe the relationship within the different positions on field and different skills
(like skill_long_passing, skill_dribbling etc.)
RO2 : To describe the relationship between the player's value and their overall ratings
RO3 : To describe the trend of different players(like defenders, midfielders, goalkeepers,
forwards) with respect to their age.
2)
RO4 : To predict the full team (means players in each position) with a specified(given) value.
RO5 : To predict the players ratings and similar players based on different skills as that of a 
specified(given) player.
3)
R06 : To defend the model for performing the prediction in RO4, RO5 using root means squared
error and R squared metrics.
4)
RO7 : To defend the model for performing the prediction in RO4, RO5 by providing insights about 
relationship between different players attributes and the rating.


Intellectual Merit: 
In this as we are getting multiple insights from the data but the new knowledge, we can get more
using predictive analytics.(Also this analysis will be based on )

1)	Minimum rating of each skill required for a player to be part of first team for given club 
    (at different positions).
2)	Creating a team having 11 players based on club budget for current season.
3)	Deciding the future transfers based on club’s budget and player's position(this is based 
on player's playing position like centre back, forward etc. and different skills combination).

Data Sourcing:  
For this project, the primary source of data will be CSV data which is readily available to
download from Kaggle which is prepared by scrapping the website https://sofifa.com. The data belongs
to the FIFA video game(EA Sports) but all the stats are calculated by EA Sport are based on real
life players performance(change rating and different attributes ratings every 3-4 months).
Also, it can be scrapped from the above website by writing our own scrapper. But I am using 
below link to download data 
URL - https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset/download?datasetVersionNumber=3


Related Work: (Please use ASU Library to open the below links)
https://ieeexplore.ieee.org/document/9208331

https://pdf.sciencedirectassets.com/271700/1-s2.0-S0377221700X04316/1-s2.0-S0377221702006847/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLWVhc3QtMSJIMEYCIQCiP9fv7bPjOhdJCGAshBgJFI96uWT6E4jv%2BgUCIMFXEwIhAJyU%2FCRhGTNFfUZ5mHr5vwfk%2FquHL76E%2FTzqbJxCntlbKswECGIQBRoMMDU5MDAzNTQ2ODY1IgyIvfMFS3YDED87Kl0qqQTQYQDJgUW%2Fbq3YBIR26dgMsKOxwqHzwbZNZW2v6yHTjKMYr2pQQD0f%2FT6x6tR%2BjZq%2BJmGuHCVgrZVF4iz9J3D9fotNt8wX9V2NDAn5rf%2B4o2r6PqO6bdYGcbxJ7R%2FRG%2BiPmxBsbv9qC8SEGIsnxbzjplR9Zbksz3B672xmUxjW8OPHGKwZ7E43zC9Ss5Fvr%2F2jJaBx%2FStCM04qPYzeQD95EXQValH4QH%2B1KnnQR2fMYaY%2FHPfsOVwY10jPZcGB1hSqJAVP%2BZqkUWx3G%2FqpmQKBS0BIGVBGppwFEsnn2djNDeVIl%2BK8Kxf7%2B6kD6IDKD%2FFqQCbipH6JdCy6qSglAxIuLWjZDH9O5w8PxF03o9e6v%2BW6iHR8fYuCgfKG9kHLaepy7IcYEXJBodhCvXoiK4p6W4rsBN4c98dSY26vgk%2FprGUbhIb2UhuiUgJ2Pua514i4vZ9qecn8hGUepJp%2BO0Dz2Zt3Upm2PaVRcnD8KKoEhhVHWkBO54o9uei664d%2BXxUjxbNFIIST7leiyY8eFYTkBvASpUv3aFmmLC0LSKM%2F6ztcOmALdrpXCL%2BAt6FHYtqVX4YdvoRclrDmOGlWDfMmuqZ5%2FEkVUEhNKn2Jpu5dfBzS0p1L7LzZR61F1TFDwkNUSgejQVt8KkERB4DX29xyuZu1TP79iCA3Rs7AoagZ%2Fn6NLEvd7VOK6LC5yqBjtUPsfs6kdtkCyC0kgLtw5KkMDLbHv7LEhVZoMMrg%2BpoGOqgBFqb29kRChKvq0%2BWG5qJzNuP5Ylg5CuOq%2BeYzSdIp%2B%2FTZhDeMfHDm6LtH4aVzOC0v%2BNfeGCACkiYGjspTHx1H%2FCm81ZPWssdiTi3FmvhpmO%2BnS77QrrTUoR4FwsK7njP8zbFQxdFN9mok5oE2UQoVIMYJpAp3t0MvNmoKni6TCfmKJhwbkIo4KwxCUp4MF5X9pDE%2BUG6j0MXfCMHHK5i7C11T28Cn9j9g&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221030T183714Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY5JGSEDFF%2F20221030%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=84dd46273a080cfe646f63360e0d6d3382edc811bbd429b26664f71ed8880025&hash=3ecaa09d3948fddcc1970afa3e8fe049c6b9018c0b21e9e4163bcf0e06fd34eb&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0377221702006847&tid=spdf-ea479036-0472-4042-8eb0-fca1e830b2ad&sid=f99e407c4319a14f1f6ae9f37bf32926bc56gxrqa&type=client&ua=51595552515404585001&rr=762642d71a93a6f4

https://towardsdatascience.com/fifa-world-cup-2018-a-data-driven-approach-to-ideal-team-line-ups-93505cfe36f8

https://www-tandfonline-com.ezproxy1.lib.asu.edu/doi/pdf/10.1080/02640414.2020.1768636?needAccess=true

https://arxiv.org/pdf/1802.04987.pdf


