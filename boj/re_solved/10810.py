N, M = map(int,input().split())
bucket = [0] * N # N 개의 바구니를 가지고 있음
for _ in range(M): # M 번 반복함
    a, b, c = map(int,input().split())
    for i in range(a,b + 1): # a번 바구니부터 b번 바구니까지 c번 공넣기
        bucket[i - 1] = c
print(*bucket)
# N제곱