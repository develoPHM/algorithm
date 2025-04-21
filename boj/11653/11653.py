N = int(input())
num = N
arr = []
i = 2
while N != 1:
    if N % i == 0:
        arr.append(i)
        N = N // i
    else:
        i += 1
for i in arr:
    print(i)