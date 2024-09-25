from collections import deque

N, M = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]
q = deque([[0,0]])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1:
                q.append([nx,ny])
                graph[ny][nx] = graph[y][x] + 1

print(graph[N-1][M-1])