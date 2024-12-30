def solution(board, moves):
    stack = []
    cnt = 0
    for c in moves:
        for i in range(len(board)):
            if board[i][c - 1] == 0:
                continue
            if stack and stack[-1] == board[i][c - 1]:
                stack.pop()
                board[i][c - 1] = 0
                cnt += 2
                break
            else:
                stack.append(board[i][c - 1])
                board[i][c - 1] = 0
                break
    return cnt