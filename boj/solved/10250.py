T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())
    count = 0
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            count += 1
            if count == N:
                print(j * 100 + i)
                