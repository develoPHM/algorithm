from itertools import combinations

N = int(input())
stat = []
for _ in range(N):
    stat.append(list(map(int,input().split())))
home = []
ans = 1e9

def find_away_team():
    away = []
    for i in range(N):
        if i in home:
            continue
        away.append(i)
    return away

def calculate_team_stat(a):
    a_sum = 0
    for pair in combinations(a, 2):
        a_sum += stat[pair[0]][pair[1]] + stat[pair[1]][pair[0]]
    return a_sum

def team(n, start):
    global ans
    if n == N // 2:
        away = find_away_team()
        home_stat = calculate_team_stat(home)
        away_stat = calculate_team_stat(away)
        diff = abs(home_stat - away_stat)
        ans = min(diff, ans)
        return
    for i in range(start, N):
        home.append(i)
        team(n + 1, i + 1)
        home.pop()


team(0, 0)
print(ans)