from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(r):
    q = deque([1])
    visited[r] = 1

    while q:
        v = q.popleft()
        for c in graph[v]:
            if visited[c] == 0:
                visited[c] = 1
                q.append(c)
                bfs(c)
bfs(1)
print(visited[2:].count(1))
