WHITE_BOARD = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
]

BLACK_BOARD = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]
# 8 x 8 그래프
# M, N = map(int, input().split())
# graph = []
# for i in range(M):
#     graph.append(input())
# for i in range(0, M - 8):
#     for j in range(0, N - 8):
#

# cur_part: 현재 바라보고 있는 부분
# board: 비교 대상 보드
M, N = map(int, input().split())
origin_board = []
for y in range(M):
    origin_board.append(input())

ans = 1e9


def count_diff(start_y, start_x, origin, other):
    diff_cnt = 0
    for i in range(8):
        for j in range(8):
            if other[i][j] != origin[start_y + i][start_x + j]:
                diff_cnt += 1
    return diff_cnt


for y in range(0, len(origin_board) - 7):
    for x in range(0, len(origin_board[0]) - 7):
        ans = min(
            ans,
            count_diff(y, x, origin_board, WHITE_BOARD),
            count_diff(y, x, origin_board, BLACK_BOARD),
        )
print(ans)