import sys
input = sys.stdin.readline

def row(x, n): # 가로
    for i in range(9):
        if n == board[x][i]: # 이미 있으면
            return False
    return True

def column(y, n): # 세로
    for i in range(9):
        if n == board[i][y]: # 이미 있으면
            return False
    return True

def square(x, y, n): # 3x3 칸
    for i in range(3):
        for j in range(3):
            if n == board[x // 3 * 3 + i][y // 3 * 3 + j]: # 칸내에 이미 있으면
                return False
    return True

def dfs(n):
    if n == len(blank): # 빈 공간 만큼 사용했으면
        for i in board: # 출력 후
            print(*i)
        exit() # 강제 종료

    for i in range(1,10):
        x = blank[n][0]
        y = blank[n][1]
        if  row(x,i) and column(y,i) and square(x, y, i):
            board[x][y] = i
            dfs(n + 1)
            board[x][y] = 0


board = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i,j])
dfs(0)