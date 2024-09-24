import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r):
    global count
    visited[r] = cnt
    li[r].sort()
    for i in li[r]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


N, M, R = map(int, input().split())
li = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)  # 저장값
count = 1
for _ in range(M):
    a, b = map(int, input().split())
    li[a].append(b)  # 양 방향 간선
    li[b].append(a)  # 양 방향 간선
dfs(R)
for i in range(1, N + 1):
    print(visited[i])
