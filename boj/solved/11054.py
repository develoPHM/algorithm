N = int(input())
up_li = list(map(int, input().split()))
down_li = up_li[::-1]
up_dp = [1] * N
down_dp = [1] * len(down_li)
m = 0

for i in range(1, N):
    for j in range(0, i):
        if up_li[i] > up_li[j]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)

for i in range(1, N):
    for j in range(0, i):
        if down_li[i] > down_li[j]:
            down_dp[i] = max(down_dp[i], down_dp[j] + 1)

down_dp = down_dp[::-1]

for i in range(N):
    m = max(m, up_dp[i] + down_dp[i])

print(m - 1)