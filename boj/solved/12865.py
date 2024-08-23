N, K = map(int, input().split())

li = [[0, 0]]
dp = [[0] * (K + 1) for _ in range(N + 1)]
for _ in range(N):
    W, V = map(int, input().split())
    li.append([W, V])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        W = li[i][0]
        V = li[i][1]
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
# dp[i][j] = max(현재물건가치 + dp[이전물건][현재 가방 무게 - 현재 물건 무게], dp[이전물건][현재 가방 무게])
            dp[i][j] = max(V + dp[i - 1][j - W], dp[i - 1][j])
print(dp[N][K])
