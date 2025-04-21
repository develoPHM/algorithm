board = [["blue", "red", "orange", "red"],
         ["red", "red", "blue", "orange"],
         ["blue", "orange", "red", "red"],
         ["orange", "orange", "red", "blue"]]

h, w = 3, 0
check = board[h][w]
cnt = 0
dx = [0, 0, -1, 1]
dy = [1, -1 ,0 ,0]
for i in range(4):
    nx = h + dx[i]
    ny = w + dy[i]
    if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
       if board[nx][ny] == check:
           cnt += 1
print(cnt)