import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 10001
li = [0] * 10001
for i in range(1, N + 1):
    li[i] = int(input())
dp[1] = li[1]
dp[2] = li[1] + li[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i-3] + li[i-1] + li[i], dp[i - 2] + li[i], dp[i - 1])

print(dp[N])