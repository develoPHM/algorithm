N, M = map(int,input().split())
li = list(map(int,input().split()))
pre_sum = [0] * N
pre_sum[0] = li[0] % M
cnt = [0] * 1001
ans = 0
for i in range(1, N):
    pre_sum[i] = (pre_sum[i - 1] + li[i]) % M
for n in pre_sum:
    cnt[n] += 1
for i in range(M):
    ans += cnt[i] * (cnt[i] - 1) // 2

print(ans + cnt[0])