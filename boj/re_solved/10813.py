N, M = map(int,input().split())
bucket = [0] * N
for i in range(N):
    bucket[i] = i + 1
for i in range(M):
    a, b = map(int,input().split())
    bucket[a - 1], bucket[b - 1] = bucket[b - 1], bucket[a - 1]
print(*bucket)