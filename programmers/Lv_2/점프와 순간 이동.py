N = 5
cnt = 0

while N > 0:
    if N % 2 == 1:
        N -= 1
        cnt += 1
    else:
        N = N // 2