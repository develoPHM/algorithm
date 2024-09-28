from collections import deque

x, y, z = map(int, input().split())
graph = [[] for _ in range(z)]
for i in range(z):
    for j in range(y):
        graph[i].append(list(map(int,input().split())))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dz = [1, -1]

def bfs():
    q = deque()
    for i in range(y):
        for j in range(x):
            if graph[i][j] == 1:
                q.append([j, i])  # 1의 위치를 큐에 넣었따

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= x or ny < 0 or ny >= y:
                continue
            if graph[ny][nx] != 0:
                continue
            graph[ny][nx] = graph[b][a] + 1
            q.append([nx, ny])