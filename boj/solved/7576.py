from collections import deque

x, y = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(y)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


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


bfs()
ans = 0
for row in graph:
    for c in row:
        if c == 0:
            print(-1)
            exit(0)
        else:
            ans = max(ans, c)
print(ans - 1)
for c in graph:
    print(c)