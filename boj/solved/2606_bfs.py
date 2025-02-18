from collections import deque

v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]
visited = [1]
for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


def bfs(r):
    q = deque([1])
    visited.append(r)
    while q:
        v = q.popleft()
        for c in graph[v]:
            if c not in visited:
                visited.append(c)
                q.append(c)
bfs(1)
print(len(visited[2:]))