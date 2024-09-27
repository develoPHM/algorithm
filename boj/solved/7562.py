from collections import deque

T = int(input())

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


def bfs(a, b):
    q = deque()
    q.append([a, b, 0])
    while q:
        x, y, cnt = q.popleft()
        if x == e1 and y == e2:
            return cnt

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if graph[ny][nx]:
                continue
            graph[ny][nx] = True
            q.append([nx, ny, cnt + 1])

for _ in range(T):
    I = int(input())
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    graph = [[False] * I for _ in range(I)]
    ans = bfs(s1, s2)
    print(ans)
