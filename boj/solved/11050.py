N, K = map(int,input().split())
up = 1
down = 1
for i in range(N, N - K, -1):
    up = i * up
for i in range(K,0,-1):
    down = i * down
print(int(up / down))