from collections import deque

def solution(maps):
    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()
            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵 벗어남
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                # 벽무시
                if maps[nx][ny] == 0:
                    continue
                # 고
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))

        return maps[len(maps) - 1][len(maps[0]) - 1]
    ans = bfs(0, 0)

    if ans == 1:
        return -1
    else:
        return ans