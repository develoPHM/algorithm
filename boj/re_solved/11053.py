N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    m = 0
    for j in range(i):
        if arr[i] > arr[j]:
            m = max(m, dp[j])
        dp[i] = m + 1
print(max(dp))