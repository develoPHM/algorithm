N = int(input())
for i in range(1,N + 1):
    num = i
    for j in str(i):
        num += int(j)
    if num == N:
        print(i)
        exit(0)
print()