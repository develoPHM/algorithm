N = int(input())
cnt = 0
check = False
while N >= 0 :
    if N % 5 == 0:
        cnt += N // 5
        check = True
        print(cnt)
        break
    N -= 3
    cnt += 1
if not check:
    print(-1)