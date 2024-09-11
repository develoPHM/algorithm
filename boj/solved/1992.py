N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

def paper(row, col, n):
    check = graph[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        paper(row, col, n)  # 오른쪽 위
        paper(row, col + n, n)  # 왼쪽 위
        paper(row + n, col, n)  # 오른쪽 아래
        paper(row + n, col + n, n)  # 왼쪽 아래
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


paper(0, 0, N)