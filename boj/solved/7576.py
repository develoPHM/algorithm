from collections import deque

x, y = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(y)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    global x, y
    q = deque()

    for i in range(y):
        for j in range(x):
            if graph[i][j] == 1:
                q.append((j, i))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(graph[0]) or ny < 0 or ny >= len(graph):
                continue
            if graph[ny][nx] != 0:
                continue
            graph[ny][nx] = graph[y][x] + 1
            q.append((nx, ny))

bfs()
ans = 0
for row in graph:
    for value in row:
        if value == 0:
            print(-1)
            exit(0)
        ans = max(ans, value)

print(ans - 1)
