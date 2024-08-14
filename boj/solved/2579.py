N = int(input())

points = [0] * 10001
for i in range(1, N + 1):
    points[i] = int(input())

dp = [0] * 10001
dp[0] = 0
dp[1] = points[1]
dp[2] = points[1] + points[2]
dp[3] = points[3] + max(points[1], points[2])

for i in range(4, N + 1):
    dp[i] = points[i] + max(dp[i - 2], dp[i - 3] + points[i - 1])

print(dp[N])
