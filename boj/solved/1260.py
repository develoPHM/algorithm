from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for c in graph:
    c.sort()

def dfs(start):
    visited_dfs[start] = 1
    print(start, end=' ')
    for c in graph[start]:
        if visited_dfs[c] == 0:
            dfs(c)


def bfs(start):
    q = deque([start])
    visited_bfs[start] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')
        graph[v].sort()
        for node in graph[v]:
            if visited_bfs[node] == 0:
                visited_bfs[node] = 1
                q.append(node)


dfs(V)
print()
bfs(V)
