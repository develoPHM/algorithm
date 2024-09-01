N = int(input())

dp = [[0] * 12 for _ in range(N + 1)] # 인덱스 접근 간편하게 좌,우 0 추가
for i in range(2, 11): # 숫자 1개일 때 1부터 9까지 가능, 0은 제외
    dp[1][i] = 1
# 그 숫자가 나타났을 때, 그 숫자 앞에 나올수 있는 수의 개수 더함.
# 예를 들어 n = 2 일 때 0이 나오면 0 앞에 1이 나와야 하므로 1
# 예를 들어 n = 2 일 때 3이 나오면 3 앞에 2, 4가 나올 수 있으므로 2
for i in range(2, N + 1):
    for j in range(1, 11):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

ans = sum(dp[N])
print(ans % 1000000000)