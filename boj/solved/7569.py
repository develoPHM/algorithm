import sys
input = sys.stdin.readline
from collections import deque

x, y, z = map(int, input().split())
graph = [[] for _ in range(z)]
for i in range(z):
    for j in range(y):
        graph[i].append(list(map(int,input().split())))
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    q = deque()
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if graph[k][j][i] == 1:
                    q.append([i, j, k])

    while q:
        a, b, c = q.popleft()
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if nx < 0 or nx >= x or ny < 0 or ny >= y or nz < 0 or nz >= z:
                continue
            if graph[nz][ny][nx] != 0:
                continue
            graph[nz][ny][nx] = graph[c][b][a] + 1
            q.append([nx, ny, nz])


bfs()
ans = 0
for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
            ans = max(ans, c)
print(ans - 1)
for c in graph:
    for a in c:
        print(a)