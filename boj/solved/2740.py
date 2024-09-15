li_1 = []
li_2 = []
N, M = map(int,input().split())
for i in range(N):
    li_1.append(list(map(int,input().split())))

M, K = map(int,input().split())
for i in range(M):
    li_2.append(list(map(int,input().split())))

li = [[0] * K for _ in range(N)]

for a in range(N):
    for b in range(K):
        for c in range(M):
            li[a][b] += li_1[a][c] * li_2[c][b]
for c in li:
    print(*c)