N, M = map(int,input().split())
bucket = [0] * N # N개의 바구니
for _ in range(M): # M번 공 넣기
    i,j,k = map(int,input().split())
    for ball in range(i, j + 1): # 버킷인덱스 i부터 j 까지 k값으로 바꾸기
        bucket[ball - 1] = k
print(*bucket)