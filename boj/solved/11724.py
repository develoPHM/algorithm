from collections import deque
import sys
input = sys.stdin.readline

def bfs(num):
    q = deque()
    q.append(num)
    v[num] = 1
    while q:
        check = q.popleft()
        for c in graph[check]:
            if v[c] == 0:
                q.append(c)
                v[c] = 1

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
v = [0] * (N + 1)
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    if v[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)