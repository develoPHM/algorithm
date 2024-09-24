import sys

input = sys.stdin.readline

N = int(input())

graph = []
result = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(a, b):
    graph[a][b] = 0
    cnt = 1
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 1:
            cnt += dfs(nx, ny)

    return cnt


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = dfs(i, j)
            result.append(count)

result.sort()

print(len(result), *result, sep='\n')
