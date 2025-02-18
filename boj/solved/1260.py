from collections import deque
N, M, V = map(int,input().split())
graph = [[] for _ in range(N + 1)]

visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

for _ in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for c in graph:
    c.sort()

def dfs(start):
    visited_dfs[start] = 1
    print(start, end=' ')
    for c in graph[start]:
        if visited_dfs[c] == 0:
            dfs(c)
print(dfs(V))