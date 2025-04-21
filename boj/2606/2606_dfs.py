cnt = 0
def dfs(start):
    global cnt
    visited[start] = 1
    for c in graph[start]:
        if visited[c] == 0:
            cnt += 1
            dfs(c)

v = int(input())
m = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
visited = [0] * (v + 1)

dfs(1)
print(cnt)