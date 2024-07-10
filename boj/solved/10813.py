N, M = map(int,input().split())
bucket = []
for i in range(1, N + 1): # 바구니에 숫자에 맞게 공 넣기
    bucket.append(i)
for _ in range(M):
    i, j = map(int,input().split())
    # 공 바꾸기
    bucket[i - 1], bucket[j - 1] = bucket[j - 1], bucket[i - 1]
print(*bucket)