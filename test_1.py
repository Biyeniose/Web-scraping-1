import requests

#data_link = "https://www.premierleague.com/match/66348"

#page = requests.get(data_link)
#page

from bs4 import BeautifulSoup

def get_data(url):
    team = 'Leicester City'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    
    global main_team_score
    global other_team_score
    global home_name
    global my_team
    global my_other_team
    global my_team_formation
    global my_other_team_formation
    global outcome
    outcome =''
    
    #get home team name
    home_team_bracket = soup.find('div', class_='team home')
    home_team = home_team_bracket.find('span', class_='long')
    
    #HOME TEAM NAME
    home_name = home_team.text
    
    #get away team name
    away_team_bracket = soup.find('div', class_='team away')
    away_team = away_team_bracket.find('span', class_='long')
    
    #AWAY TEAM NAME
    away_name = away_team.text
    
    #get home and away formations
    #home_formation = ''
    #away_formation = ''
    the_formation = []
    formation = soup.find_all('div', class_='position')
    
    for loop_in_players_list in formation:
        #print(loop_in_players_list.strong.text)
        the_formation.append(loop_in_players_list.strong.text)
    
    #HOME TEAM FORMATION
    home_formation = the_formation[0] 
    
    #AWAY TEAM FORMATION
    away_formation = the_formation[1]
    

    #get the score of the game
    score_match = soup.find('div', class_='score fullTime')
    score = score_match.text
    #print(score)
    
    #HOME TEAM GOALS
    home_team_score = score[0]
    
    #AWAY TEAM GOALS
    away_team_score = score[2]
    
    
    #determines which team is the team in question
    
    #index 0 is for the main team formation and index 1 is for other team
    global formations
    formations = ['','']
    
    global goals_scored
    goals_scored = ['','']
    
    if home_name == (team):
        my_team = home_name
        my_other_team = away_name
        
        #index 0 is for the main team formation and index 1 is for other team
        formations[0] = the_formation[0]
        formations[1] = the_formation[1]
        
        goals_scored[0] = score[0]
        goals_scored[1] = score[2]
        
        
                  
        
    elif away_name == (team):
        my_team = away_name
        my_other_team = home_name
        
        #index 0 is for the main team formation and index 1 is for other team
        formations[0] = the_formation[1]
        formations[1] = the_formation[0]
        
        goals_scored[0] = score[2]
        goals_scored[1] = score[0]
        
    if (goals_scored[0])>(goals_scored[1]):
        outcome = 'W'
    elif (goals_scored[0])<(goals_scored[1]):
        outcome = 'L'
    elif (goals_scored[0])==(goals_scored[1]):
        outcome = 'D'
        
    ata_link = "https://www.premierleague.com/match/58902"
get_data(data_link)
gameweek_number = 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')


data_link = "https://www.premierleague.com/match/58911"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')


data_link = "https://www.premierleague.com/match/58921"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/58931"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/58940"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

#gameweek 6
data_link = "https://www.premierleague.com/match/58946"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/58959"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/58971"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/58982"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/58991"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59002"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59011"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59020"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59034"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59040"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59049"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59062"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59080"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59080"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59088"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59101"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59108"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59125"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59131"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59137"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59150"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59177"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59157"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59171"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59191"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59205"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59211"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59220"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59233"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59240"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59249"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59258"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')

data_link = "https://www.premierleague.com/match/59270"
get_data(data_link)
gameweek_number += 1
print(f"Gameweek {gameweek_number}:  {home_name} vs {away_name}  <==>  {outcome}  <==> Formation = {formations[0]}")
print('')
