N = int(input())

li = [0] * 301
for i in range(1, N + 1):
    li[i] = int(input())
dp = [0] * 301
dp[1] = li[1]
dp[2] = li[1] + li[2]
dp[3] = max(li[1] + li[3], li[2] + li[3])
for i in range(4, N + 1):
    dp[i] = max(li[i] + dp[i - 2], li[i] + li[i - 1] + dp[i - 3])

print(dp[N])