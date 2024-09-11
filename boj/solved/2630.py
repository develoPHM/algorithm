N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0

def paper(row, col, n):
    global blue, white
    check = graph[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        n = n // 2
        paper(row, col, n)
        paper(row + n, col, n)
        paper(row, col + n, n)
        paper(row + n, col + n, n)
    elif check == 1:
        blue += 1
    elif check == 0:
        white += 1


paper(0, 0, N)
print(white)
print(blue)