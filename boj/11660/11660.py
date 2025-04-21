import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

sum_graph = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_graph[i][j] = sum_graph[i][j - 1] + sum_graph[i - 1][j] - sum_graph[i - 1][j - 1] + graph[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sum_graph[x2][y2] - sum_graph[x2][y1 - 1] - sum_graph[x1 - 1][y2] + sum_graph[x1 - 1][y1 - 1]
    print(ans)
