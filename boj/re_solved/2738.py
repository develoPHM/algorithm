N, M = map(int,input().split())
g1 = []
g2 = []
for i in range(N):
    g1.append(list(map(int,input().split())))
for i in range(N):
    g2.append(list(map(int,input().split())))
for i in range(N):
    for j in range(M):
        g1[i][j] += g2[i][j]
for c in g1:
    print(*c)
# 시간복잡도 O(1)