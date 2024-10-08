from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = []
result = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                count += 1

    return count


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(i, j)
            result.append(count)

result.sort()

print(len(result), *result, sep='\n')