from urllib.request import urlopen
import math
import time
import datetime

exiled_url = "https://eune.op.gg/summoner/userName=Ex1L3d"
mr_gummy_url = "https://eune.op.gg/summoner/userName=MrGummy"

RANK_TAG = '<meta name="description"'


def extract_rank(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")

    rank_position = html.find(RANK_TAG)
    rank_snippet = html[rank_position: rank_position + 100]
    rank_string = rank_snippet.split("/")[1]

    return rank_string.split(" ")[1:4]

def calculate_difference(rank_one, rank_two):
    diff = 0
    div_one = int(rank_one[1])
    div_two = int(rank_two[1])
    lp_one = int(rank_one[2][:-2])
    lp_two = int(rank_two[2][:-2])

    if div_one - div_two < 0:
        diff += 100 * (div_two - div_one)

    diff += (lp_one - lp_two)

    return diff

def legendary_platinum_battle():
    mess = ''
    exiled_rank = extract_rank(exiled_url)
    mr_gummy_rank = extract_rank(mr_gummy_url)

    mess += "EXILED RANK: " + " ".join(exiled_rank) + '\n'
    mess += "MRGUMMY RANK: " + " ".join(mr_gummy_rank) + '\n'

    diff = calculate_difference(exiled_rank, mr_gummy_rank)

    if(diff <= 0):
        mess += """
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░█▀▀▀░█▀▀▀░░█▀▀░▀▀█░░█░░░░
    ░░░░█░▀█░█░▀█░░█▀▀░▄▀░░░▀░░░░
    ░░░░▀▀▀▀░▀▀▀▀░░▀▀▀░▀▀▀░░▀░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    """ + "WE DID IT BOYS!!!"
    else:
        mess +=  f'{diff} LP difference\n'
        mess += f"{math.ceil(diff / 15)} games to close the gap (assuming +15, -15)"
    return mess

def neverending_climb():
    curr_time = datetime.datetime.now().timestamp()
    start_time = curr_time - 60 * 60 * 24
    page = urlopen(exiled_url)
    html = page.read().decode("utf-8")
    wins = 0
    loses = 0
    index = 0
    mess = ""
    while index < len(html):
        index = html.find('data-game-time', index)
        if index == -1:
            break
        mtime = html[index:index+50].split("\"")[1]
        print('time', mtime)
        if int(mtime) < start_time:
            break
        index = html.find('data-game-result', index)
        result = html[index:index+50].split("\"")[1]
        print('result', result)
        if result == "win":
            wins += 1
        elif result == "lose":
            loses += 1
        index = html.find('champion/', index)
        champion = html[index:index+50].split("/")[1]
        diff = time.strftime("%H:%M:%S", time.localtime(curr_time - int(mtime)))
        mess += f"{champion} {result} {diff}\n"
    return f"In the last 24 hours Ex1l3d won {wins} games and lost {loses} games\n" + mess