import sys
input = sys.stdin.readline
N = int(input())
stat = []
for _ in range(N):
    stat.append(list(map(int, input().split())))

team = [False] * N
ans = 1e9

def separate_teams(t):
    home = []
    away = []
    for i in range(N):
        if t[i]:
            home.append(i)
        else:
            away.append(i)
    return home, away

def cal(a):
    a_sum = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            a_sum += stat[a[i]][a[j]] + stat[a[j]][a[i]]
    return a_sum


def backtrack(n, start):
    global ans
    if n == N // 2:
        home, away = separate_teams(team)
        # print('home:', home, cal(home))
        # print('away:', away, cal(away))
        ans = min(ans , abs(cal(home) - cal(away)))
        return

    for i in range(start, N):
        team[i] = True
        backtrack(n + 1, i + 1)
        team[i] = False


backtrack(0, 0)
print(ans)
