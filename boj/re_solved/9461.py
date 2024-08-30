import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
for i in range(5,100):
    dp[i] = dp[i - 1] + dp[i - 5]
for _ in range(N):
    a = int(input())
    print(dp[a-1])