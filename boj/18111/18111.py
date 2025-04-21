N, M, B = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

# 판떼기 전체 평균
board_sum = 0
for c in board:
    board_sum += sum(c)