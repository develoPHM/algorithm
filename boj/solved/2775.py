T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    down = []
    for i in range(n):
        down.append(i + 1)

    for i in range(k):
        up = []
        sum = 0
        for j in range(n):
            sum += down[j]
            up.append(sum)
        down = up
    print(up[-1])