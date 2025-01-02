def solution(players, callings):
    dic = {}

    for i in range(len(players)):
        dic[players[i]] = i

    for i in callings:
        win = dic[i] - 1
        lose = dic[i]

        players[win], players[lose] = players[lose], players[win]
        dic[players[win]], dic[players[lose]] = win, lose
    return players
