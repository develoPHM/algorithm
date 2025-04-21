n = int(input())
li = [0] * 10001
dp = [0] * 10001
for i in range(1, n + 1):
    li[i] = int(input())

dp[1] = li[1]
dp[2] = li[1] + li[2]
dp[3] = max(li[1] + li[2], li[1] + li[3], li[2] + li[3])
for i in range(4, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 3] + li[i] + li[i - 1], li[i] + dp[i - 2])
print(dp[n])
