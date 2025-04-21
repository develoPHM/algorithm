N, M = map(int,input().split())
li = list(map(int,input().split()))
pre_sum = [0] * N
pre_sum[0] = li[0] % M
count = [0] * 1001
ans = 0
for i in range(1, N):
    pre_sum[i] = (pre_sum[i - 1] + li[i]) % M
for n in pre_sum:
    count[n] += 1
for i in range(M):
    ans += count[i] * (count[i] - 1) // 2

print(ans + count[0])