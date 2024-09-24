N = int(input())
arr = list(map(int,input().split()))
count = 0
for num in arr:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        count += 1
print(count)