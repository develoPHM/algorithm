N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
sum_minus = 0
sum_one = 0
sum_zero = 0


def paper(row, col, n):
    global sum_one, sum_zero, sum_minus
    check = graph[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if check != graph[i][j]:
                check = 2
                break
    if check == 2:
        n = n // 3
        paper(row, col, n)
        paper(row, col + n, n)
        paper(row, col + 2 * n, n)
        paper(row + n, col, n)
        paper(row + n, col + n, n)
        paper(row + n, col + 2 * n, n)
        paper(row + 2 * n, col, n)
        paper(row + 2 * n, col + n, n)
        paper(row + 2 * n, col + 2 * n, n)

    elif check == -1:
        sum_minus += 1
    elif check == 0:
        sum_zero += 1
    else:
        sum_one += 1
paper(0, 0, N)
print(sum_minus)
print(sum_zero)
print(sum_one)