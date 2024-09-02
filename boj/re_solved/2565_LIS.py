N = int(input())
line = []
li = []
dp = [1] * N
for _ in range(N):
    line.append(list(map(int, input().split())))
line.sort(key=lambda x: x[0])
for i in range(N):
    li.append(line[i][1])

for i in range(N):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[j] + 1, dp[i])
print(N - max(dp))
