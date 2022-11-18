#### SER594: Experimentation
#### Soccer Team and Similar Player Selection (title)
#### Amarjeet Singh (author)
#### 21 November 2022 (date)


## Explainable Records
### Record 1
**Raw Data:** 
sofifa_id,player_url,short_name,long_name,player_positions,overall,potential,value_eur,wage_eur,age,dob,height_cm,weight_kg,club_team_id,club_name,league_name,league_level,club_position,club_jersey_number,club_loaned_from,club_joined,club_contract_valid_until,nationality_id,nationality_name,nation_team_id,nation_position,nation_jersey_number,preferred_foot,weak_foot,skill_moves,international_reputation,work_rate,body_type,real_face,release_clause_eur,player_tags,player_traits,pace,shooting,passing,dribbling,defending,physic,attacking_crossing,attacking_finishing,attacking_heading_accuracy,attacking_short_passing,attacking_volleys,skill_dribbling,skill_curve,skill_fk_accuracy,skill_long_passing,skill_ball_control,movement_acceleration,movement_sprint_speed,movement_agility,movement_reactions,movement_balance,power_shot_power,power_jumping,power_stamina,power_strength,power_long_shots,mentality_aggression,mentality_interceptions,mentality_positioning,mentality_vision,mentality_penalties,mentality_composure,defending_marking_awareness,defending_standing_tackle,defending_sliding_tackle,goalkeeping_diving,goalkeeping_handling,goalkeeping_kicking,goalkeeping_positioning,goalkeeping_reflexes,goalkeeping_speed,ls,st,rs,lw,lf,cf,rf,rw,lam,cam,ram,lm,lcm,cm,rcm,rm,lwb,ldm,cdm,rdm,rwb,lb,lcb,cb,rcb,rb,gk,player_face_url,club_logo_url,club_flag_url,nation_logo_url,nation_flag_url
158023,https://sofifa.com/player/158023/lionel-messi/150002,L. Messi,Lionel Andrés Messi Cuccittini,CF,93,95,100500000.0,550000.0,27,1987-06-24,169,67,241.0,FC Barcelona,Spain Primera Division,1,CF,10,,2004-07-01,2018,52,Argentina,1369.0,CF,10,Left,3,4,5,Medium/Low,Normal (170-),Yes,,"#Speedster, #Dribbler, #FK Specialist, #Acrobat, #Clinical Finisher, #Complete Forward","Finesse Shot, Speed Dribbler (AI), One Club Player, Team Player",93,89,86,96,27,63,84,94,71,89,85,96,89,90,76,96,96,90,94,94,95,80,73,77,60,88,48,22,92,90,76,,25,21,20,6,11,15,14,8,,89+3,89+3,89+3,92+3,90+3,90+3,90+3,92+3,92+3,92+3,92+3,90+3,79+3,79+3,79+3,90+3,62+3,62+3,62+3,62+3,62+3,54+3,45+3,45+3,45+3,54+3,15+3,https://cdn.sofifa.net/players/158/023/15_120.png,https://cdn.sofifa.net/teams/241/60.png,https://cdn.sofifa.net/flags/es.png,https://cdn.sofifa.net/teams/1369/60.png,https://cdn.sofifa.net/flags/ar.png

Above shows the raw record but the below shows the data/attributes used in the model training and
prediction

'potential','club_position', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic','attacking_crossing', 'attacking_finishing','attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys', 'skill_dribbling','skill_curve','skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control', 'movement_acceleration','movement_sprint_speed','movement_agility', 'movement_reactions', 'movement_balance', 'power_shot_power', 'power_jumping','power_stamina','power_strength', 'power_long_shots', 'mentality_aggression', 'mentality_interceptions','mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure','defending_marking_awareness','defending_standing_tackle', 'defending_sliding_tackle', 'goalkeeping_diving','goalkeeping_handling', 'goalkeeping_kicking','goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed', 'preferred_foot','weak_foot','age', 'height_cm', 'weight_kg', 'year'

Prediction Explanation: 
The ratings has been processed on the basis of club position(playing position means defense, midfielder, forward) 
and skills that are taken to build the model. The model has predicted has overall value 91. Here the
players has position has playing position of Centre Forward and attributes like attacking_shooting,
pace and shooting has higher values so the overall value is also high. So the model is predicting 
rightly based on the other attributes value.

### Record 2
**Raw Data:** 
sofifa_id,player_url,short_name,long_name,player_positions,overall,potential,value_eur,wage_eur,age,dob,height_cm,weight_kg,club_team_id,club_name,league_name,league_level,club_position,club_jersey_number,club_loaned_from,club_joined,club_contract_valid_until,nationality_id,nationality_name,nation_team_id,nation_position,nation_jersey_number,preferred_foot,weak_foot,skill_moves,international_reputation,work_rate,body_type,real_face,release_clause_eur,player_tags,player_traits,pace,shooting,passing,dribbling,defending,physic,attacking_crossing,attacking_finishing,attacking_heading_accuracy,attacking_short_passing,attacking_volleys,skill_dribbling,skill_curve,skill_fk_accuracy,skill_long_passing,skill_ball_control,movement_acceleration,movement_sprint_speed,movement_agility,movement_reactions,movement_balance,power_shot_power,power_jumping,power_stamina,power_strength,power_long_shots,mentality_aggression,mentality_interceptions,mentality_positioning,mentality_vision,mentality_penalties,mentality_composure,defending_marking_awareness,defending_standing_tackle,defending_sliding_tackle,goalkeeping_diving,goalkeeping_handling,goalkeeping_kicking,goalkeeping_positioning,goalkeeping_reflexes,goalkeeping_speed,ls,st,rs,lw,lf,cf,rf,rw,lam,cam,ram,lm,lcm,cm,rcm,rm,lwb,ldm,cdm,rdm,rwb,lb,lcb,cb,rcb,rb,gk,player_face_url,club_logo_url,club_flag_url,nation_logo_url,nation_flag_url
13121,225291,G. Sciacca,CB,58,75,90000.0,2000.0,18,1996-04-19,180,75,44.0,Inter,Italian Serie A,1.0,RES,24.0,2013-07-01,2021.0,27,Italy,Right,3,2,1,Low/High,Lean (170-185),9000.0,No traits available,60.0,32.0,34.0,44.0,61.0,56.0,37,27,55,36,31,38,28,33,29,46,58,62,49,57,65,49,74,55,55,24,55,58,28,32,41,57.78757218882875,62,64,62,12,6,15,13,8,39.53150528782218,13,2015

Prediction Explanation:** 
As the above-mentioned record is of defensive player(i.e. Centre Back) and attributes like defending, physic,
skill_long_passing, passing, defending_standing_tackle, defending_sliding_tackle impact the overall rating.
So the above record is having less rating for these attributes so the model predicted the lower overall rating 
i.e. 55 and there is still marginal error than the actual rating i.e. 58

## Interesting Features
### Feature A
**Feature:** 
Pace

**Justification:** 
The Pace is an important attribute for each type of athlete whether it be a soccer player or any 
other field games. 

### Feature B
**Feature:** TODO

**Justification:** TODO

## Experiments 
### Varying A
**Prediction Trend Seen:** TODO

### Varying B
**Prediction Trend Seen:** TODO

### Varying A and B together
**Prediction Trend Seen:** TODO


### Varying A and B inversely
**Prediction Trend Seen:** TODO

(duplicate above as many times as needed; remove this line when done)