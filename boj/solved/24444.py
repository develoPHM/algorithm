from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int,input().split())
cnt = 1
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(r):
    global cnt
    q = deque([r])
    visited[r] = 1

    while q:
        v = q.popleft()
        graph[v].sort()
        for node in graph[v]:
            if visited[node] == 0:
                cnt += 1
                visited[node] = cnt
                q.append(node)

bfs(R)

for c in visited[1:]:
    print(c)