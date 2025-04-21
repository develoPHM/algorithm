from collections import deque

def bfs(x, y):
    global cnt
    q.append([x, y])
    graph[x][y] = 'O'
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (0 <= nx < N and 0 <= ny < M) and graph[nx][ny] != 'X':
                # 사람일 경우
                if graph[nx][ny] == 'P':
                    cnt += 1
                graph[nx][ny] = 'X'
                q.append([nx, ny])

N, M = map(int, input().split())
q = deque()
cnt = 0
graph = []
start = [0, 0]
for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] == 'I':
            start = [i, j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

bfs(start[0], start[1])
if cnt == 0:
    print('TT')
else:
    print(cnt)