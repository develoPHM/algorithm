import sys
sys.setrecursionlimit(10**5)
T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    graph[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue
        if graph[ny][nx] == 1:
            dfs(nx, ny)


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
                dfs(i, j)
                bug += 1
    print(bug)
