#### SER594: Exploratory Data Munging and Visualization
#### Soccer Team Selection (title)
#### Amarjeet Singh
#### 23 October 2022


## Basic Questions
**Dataset Author(s):** STEFANO LEONE(He used a scrapper to scrap the data from the https://sofifa.com/ website where
there are complete details about each player)

**Dataset Construction Date:** 1 year ago

**Dataset Record Count:** As there is data related to rating of players from 2015 to 2022. In each file there are approx
18000 records and in total there are 142079 records

**Dataset Field Meanings:** The data fields are about each player's attributes like name, height, weight, 
body type etc., and mostly are about a player soccer's attributes like position of play, pace, shooting etc. 

**Dataset File Hash(es):** The below hash values has been converted to readable hexadecimal form. Please refer to
calculate_md5 function in wf_dataprocessing.py file
players_22.csv: 53035c7cb7ceeecc1726e9ef523166e5
players_21.csv: 81e3891036bb62508ead1630a5204325
players_20.csv: 81ec3f4dc5ce98d7401710a815d3b9ff
players_18.csv: 606b723d9b7ed2174a04549032f4fce6
players_19.csv: b6a7e1517bab432bec847ede3c6ff672
players_17.csv: d61f63a909c639a2b4c8c88fe5c7119e
players_16.csv: 27d444cc47d581f2d663d3c5bb978c10
players_15.csv: 22c1bbda94a36862bd22e123662235ee

## Interpretable Records
### Record 1
**Raw Data:** 
sofifa_id,player_url,short_name,long_name,player_positions,overall,potential,value_eur,wage_eur,age,dob,height_cm,weight_kg,club_team_id,club_name,league_name,league_level,club_position,club_jersey_number,club_loaned_from,club_joined,club_contract_valid_until,nationality_id,nationality_name,nation_team_id,nation_position,nation_jersey_number,preferred_foot,weak_foot,skill_moves,international_reputation,work_rate,body_type,real_face,release_clause_eur,player_tags,player_traits,pace,shooting,passing,dribbling,defending,physic,attacking_crossing,attacking_finishing,attacking_heading_accuracy,attacking_short_passing,attacking_volleys,skill_dribbling,skill_curve,skill_fk_accuracy,skill_long_passing,skill_ball_control,movement_acceleration,movement_sprint_speed,movement_agility,movement_reactions,movement_balance,power_shot_power,power_jumping,power_stamina,power_strength,power_long_shots,mentality_aggression,mentality_interceptions,mentality_positioning,mentality_vision,mentality_penalties,mentality_composure,defending_marking_awareness,defending_standing_tackle,defending_sliding_tackle,goalkeeping_diving,goalkeeping_handling,goalkeeping_kicking,goalkeeping_positioning,goalkeeping_reflexes,goalkeeping_speed,ls,st,rs,lw,lf,cf,rf,rw,lam,cam,ram,lm,lcm,cm,rcm,rm,lwb,ldm,cdm,rdm,rwb,lb,lcb,cb,rcb,rb,gk,player_face_url,club_logo_url,club_flag_url,nation_logo_url,nation_flag_url
158023,https://sofifa.com/player/158023/lionel-messi/150002,L. Messi,Lionel Andrés Messi Cuccittini,CF,93,95,100500000.0,550000.0,27,1987-06-24,169,67,241.0,FC Barcelona,Spain Primera Division,1,CF,10,,2004-07-01,2018,52,Argentina,1369.0,CF,10,Left,3,4,5,Medium/Low,Normal (170-),Yes,,"#Speedster, #Dribbler, #FK Specialist, #Acrobat, #Clinical Finisher, #Complete Forward","Finesse Shot, Speed Dribbler (AI), One Club Player, Team Player",93,89,86,96,27,63,84,94,71,89,85,96,89,90,76,96,96,90,94,94,95,80,73,77,60,88,48,22,92,90,76,,25,21,20,6,11,15,14,8,,89+3,89+3,89+3,92+3,90+3,90+3,90+3,92+3,92+3,92+3,92+3,90+3,79+3,79+3,79+3,90+3,62+3,62+3,62+3,62+3,62+3,54+3,45+3,45+3,45+3,54+3,15+3,https://cdn.sofifa.net/players/158/023/15_120.png,https://cdn.sofifa.net/teams/241/60.png,https://cdn.sofifa.net/flags/es.png,https://cdn.sofifa.net/teams/1369/60.png,https://cdn.sofifa.net/flags/ar.png

**Interpretation:** The above records gives us the information about a player named as L. Messi. This gives us info
about his height, weight, the club he is playing for, his nationality and other soccer attributes like his weak foot 
rating, his pace, his shooting etc. Most of the column names are self-explanatory except some values like ls,st,rs
and so on. These columns heading is the position of player on a soccer field(like st means striker, cb means centre back)
specifically gives us the rating of that player if he plays in this position.  The data seems reasonable as the most of
the attributes such as height_cm, age, player-value in Euros. The thing that need to be taken care is that some 
attributes has been rated in the range of 1-5 and other has been rated in range of 1-100. 
So this need to be taken care while processing

### Record 2
**Raw Data:** 
sofifa_id,player_url,short_name,long_name,player_positions,overall,potential,value_eur,wage_eur,age,dob,height_cm,weight_kg,club_team_id,club_name,league_name,league_level,club_position,club_jersey_number,club_loaned_from,club_joined,club_contract_valid_until,nationality_id,nationality_name,nation_team_id,nation_position,nation_jersey_number,preferred_foot,weak_foot,skill_moves,international_reputation,work_rate,body_type,real_face,release_clause_eur,player_tags,player_traits,pace,shooting,passing,dribbling,defending,physic,attacking_crossing,attacking_finishing,attacking_heading_accuracy,attacking_short_passing,attacking_volleys,skill_dribbling,skill_curve,skill_fk_accuracy,skill_long_passing,skill_ball_control,movement_acceleration,movement_sprint_speed,movement_agility,movement_reactions,movement_balance,power_shot_power,power_jumping,power_stamina,power_strength,power_long_shots,mentality_aggression,mentality_interceptions,mentality_positioning,mentality_vision,mentality_penalties,mentality_composure,defending_marking_awareness,defending_standing_tackle,defending_sliding_tackle,goalkeeping_diving,goalkeeping_handling,goalkeeping_kicking,goalkeeping_positioning,goalkeeping_reflexes,goalkeeping_speed,ls,st,rs,lw,lf,cf,rf,rw,lam,cam,ram,lm,lcm,cm,rcm,rm,lwb,ldm,cdm,rdm,rwb,lb,lcb,cb,rcb,rb,gk,player_face_url,club_logo_url,club_flag_url,nation_logo_url,nation_flag_url
214725,https://sofifa.com/player/214725/sam-ramsbottom/150002,S. Ramsbottom,Sam Ramsbottom,GK,42,52,20000.0,2000.0,18,1996-04-03,196,80,15048.0,Tranmere Rovers,English League Two,4,RES,20,,2013-04-01,2016,14,England,,,,Right,2,1,1,Medium/Medium,Normal (185+),No,,,,,,,,,,25,25,25,25,25,25,25,25,25,25,44,40,38,34,30,20,60,38,40,25,21,25,25,25,20,,25,25,25,50,36,44,41,44,42,27,27,27,28,27,27,27,28,27,27,27,28,27,27,27,28,28,27,27,27,28,27,28,28,28,27,42,https://cdn.sofifa.net/players/214/725/15_120.png,https://cdn.sofifa.net/teams/15048/60.png,https://cdn.sofifa.net/flags/gb-eng.png,,https://cdn.sofifa.net/flags/gb-eng.png

**Interpretation:** The interpretation is same as above. The data is in the desired range. There is no value which seems 
to be out of box for that column vaues.Yes there are some missing values which needs to be taken care in preprocessing

## Data Sources
**URL:** https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset/download?datasetVersionNumber=3
Please download the complete zip file from above URL and extract it. File names starting with players_*.csv are only used 
in this project. So MD5 is also calculated for those only.

### Transformation N
**Description:** Removing the columns that the not required

**Soundness Justification:** In this transformation, I am removing the columns that are either redundant or we will not
use these in our processing.

**Description:** Filling the null values

**Soundness Justification:** In this transformation, the null values are filled accordingly. Means some of the column
values are filled using mean, some are filled using median and some are filled with a string value.


## Visualization
### Visual 1(Age and Height Plot)
**Analysis:** As per the plot, the age of the graph is between 15 years to 55 years and there are very less number of
players more than 40 years in our data set. Also, the height is between 150 cm and 210 cm

### Visual 2(Age and Pace Plot)
**Analysis:** As per the plot, the age and pace is having inverse relationship after the age of 25 years. The player
having maximum pace is 24/25 years of age. Also, for the players more than 40 years has very less pace in comparison to
other age groups

### Visual 3(Height and Pace Plot)
**Analysis:** In this plot, we can see that average pace of players having height less than 160 cm is more than average
of other age groups. Apart from this, all the players having height more than 200 cm is having pace less than 
80(out of 100)

### Visual 4(Nation ID Plot)
**Analysis:** In this plot there are very few players from nations having nation id more than 190. Also, 
more players in the dataset belong to 0-50 country ID range.

### Visual 5(Club Jersey Plot)
**Analysis:** From this plot, it shows that most players prefer jersey number from 1 to 10 and there are few players 
who wear jersey number more than 40.


