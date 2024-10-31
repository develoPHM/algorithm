# [0, 1, 2, 3, 5, 8, 13, 21, 34, 55,
n = int(input())
dp = [0] * 1001
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i -1] + dp[i - 2]
for i in range(3, n + 1):
    dp[i] = dp[i] + dp[i] // 2
print(dp)