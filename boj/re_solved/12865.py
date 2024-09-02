N, K = map(int, input().split())

li = [[0, 0]]
for _ in range(N):
    li.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    W = li[i][0]
    V = li[i][1]
    for j in range(K + 1):
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)

print(max(dp[-1]))

# 0  A  B  C  D
# 0  0  0  0  0
# 1  0  0  0  0
# 2  0  0  0  0
# 3  0  0  6  6
# 4  0  8  8  8
# 5  0  0  0 12
# 6 13 13 13 13
# 7  0  0 14 14