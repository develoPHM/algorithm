N = int(input())
ans = 1
if N == 0:
    print(1)
    exit(0)
for i in range(1,N + 1):
    ans *= i
print(ans)