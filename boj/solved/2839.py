N = int(input())
count = 0
check = False
while N >= 0:
    if N % 5 == 0:
        count += N // 5
        check = True
        print(count)
        break
    N -= 3
    count += 1
if not check:
    print(-1)
