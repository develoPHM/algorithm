N = int(input())
line = []
for _ in range(N):
    line.append(list(map(int, input().split())))
line.sort(key=lambda x: x[0])
lis = []
dp = [1] * N
for i in range(len(line)):
    lis.append(line[i][1])
for i in range(1, N):
    for j in range(0, i):
        if lis[i] > lis[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))
