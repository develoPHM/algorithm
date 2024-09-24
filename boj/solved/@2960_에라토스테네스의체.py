N, K = map(int, input().split())
arr = [True] * (N + 1)
arr[0] = False
arr[1] = False
count = 0

for i in range(2, N + 1):
    if arr[i]:
        for j in range(i, N + 1, i):
            if arr[j]:
                arr[j] = False
                count += 1
                if count == K:
                    print(j)
                    break
