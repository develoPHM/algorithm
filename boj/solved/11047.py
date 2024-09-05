N, K = map(int,input().split())
coin = []
cnt = 0
for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
while K > 0:
    for c in coin:
        if c <= K:
            cnt += K // c
            plus = K % c
            K = K - (K // c) * c
            break
print(cnt)
