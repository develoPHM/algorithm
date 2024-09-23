N = int(input())
arr = list(map(int,input().split()))
cnt = 0
for num in arr:
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        cnt += 1
print(cnt)