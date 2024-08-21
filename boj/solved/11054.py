N = int(input())
li = list(map(int, input().split()))
dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j] + 1)
point = max(dp)
line = dp.index(point)
li_re = sorted(li[line:], reverse=True)
dp2 = [1] * len(li_re)
for i in range(1, len(li_re)):
    for j in range(0, i):
        if li_re[i] > li_re[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
point2 = max(dp2)
print(dp)
print(point)
print(dp2)
print(point + point2 - 1)
