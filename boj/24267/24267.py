n = int(input())
sum = 0
# n = 7이면  5 4 3 2 1
for i in range(1,n - 1):
    sum += (i + 1) * i // 2
print(sum)
print(3)