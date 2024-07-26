WB = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW']
BB = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB']

M, N = map(int, input().split())
board = []
for i in range(M):
    board.append(input())


def check_v2(a, b, origin, compare):
    diff = 0
    for y in range(8):
        for x in range(8):
            if origin[y + a][x + b] != compare[y][x]:
                diff += 1

    return diff


# def check(a, b,WB, BB):
#     WB_cnt = 0
#     BB_cnt = 0
#     for i in range(8):
#         for j in range(8):
#             if board[i + a][j + b] != WB[i][j]:
#                 WB_cnt += 1
#             if board[i + a][j + b] != BB[i][j]:
#                 BB_cnt += 1
#     return min(WB_cnt, BB_cnt)

ans = 65

for i in range(M - 7):
    for j in range(N - 7):
        ans = min(ans, check_v2(i, j, board, WB), check_v2(i, j, board, BB))

print(ans)
