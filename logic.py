from os import name
from queries import *
from authentication import *
from difflib import get_close_matches
import json

sheet_id = json.loads(open ('data.json', "r").read())["sheet_id"]
names = ["Player A", "Player B"]
service = None
champions = None

def initialize():
    global service, names, champions
    service = authentication.get_service()
    names = get_names(service, sheet_id)
    champions = get_champions(service, sheet_id)
    
def update():
    global names, champions
    names = get_names(service, sheet_id)
    champions = get_champions(service, sheet_id)
    
def calc_total_score():
    score = get_total_score(service, sheet_id)
    return f"""1v1 final score:\n{names[0]}: {score[0]}\n{names[1]}: {score[1]}"""

def calc_champion_score(champion):
    poss = get_close_matches(champion.capitalize(), champions, 1)
    if len(poss) == 0:
        return f'no champion with name "{champion}"'
    real = poss[0]
    start = f"Showing results for champion {real}\n"
    row = -1
    for i in range(len(champions)):
        if champions[i] == real:
            row = i+3
            break
    res = get_champion_score(service, sheet_id, row)
    score = [0, 0]
    if len(res) == 1:
        score = res[0]    
        while len(score) < 2:
            score.append(0)
        if score[0] == "":
            score[0] = 0
    return start + f"{names[0]}: {score[0]}\n{names[1]}: {score[1]}"

def calc_write_win(player, champion):
    poss = get_close_matches(champion.capitalize(), champions, 1)
    if len(poss) == 0:
        return f'no champion with name "{champion}"'
    real = poss[0]
    row = -1
    for i in range(len(champions)):
        if champions[i] == real:
            row = i+3
            break
    column = ""
    if player.lower() == names[0].lower():
        column = "B"
    elif player.lower() == names[1].lower():
        column = "C"
    if column == "":
        return f'no player with name {player}'
    # update
    cell = column + str(row)
    increment(service, sheet_id, cell)
    
    start = f"Saved a win for player {player} on champion {real}\nShowing updated results for {real}\n"
    res = get_champion_score(service, sheet_id, row)
    score = [0, 0]
    if len(res) == 1:
        score = res[0]    
        while len(score) < 2:
            score.append(0)
        if score[0] == "":
            score[0] = 0
    return start + f"{names[0]}: {score[0]}\n{names[1]}: {score[1]}"

def calc_update():
    update()
    return "Updated"