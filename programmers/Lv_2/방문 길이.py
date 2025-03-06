def solution(dirs):
    visited = set()  # (row, col, next_row, next_col) 형태로 저장
    row, col = 5, 5  # 중앙에서 시작
    cnt = 0

    move = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    for c in dirs:
        new_row = row + move[c][0]
        new_col = col + move[c][1]

        # 범위 밖이면 무시
        if new_row < 0 or new_row >= 11 or new_col < 0 or new_col >= 11:
            continue

        # (현재 위치, 이동한 위치)를 튜플로 저장 (양방향 체크)
        if (row, col, new_row, new_col) not in visited:
            visited.add((row, col, new_row, new_col))
            visited.add((new_row, new_col, row, col))  # 반대 방향도 추가
            cnt += 1

        # 현재 위치 갱신
        row, col = new_row, new_col

    return cnt