N = 5
graph = [[] for _ in range(N + 1)]
for _ in range(N):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)
print(graph)
