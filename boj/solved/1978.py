N = int(input())
arr = list(map(int,input().split()))
cnt = 0
for num in arr:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        cnt += 1
print(cnt)