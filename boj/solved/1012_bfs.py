from collections import deque

T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append([nx,ny])


for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    bug = 0
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                graph[j][i] = 0
                bfs(i, j)
                bug += 1
    print(bug)
