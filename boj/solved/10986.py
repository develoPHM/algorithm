import sys
input = sys.stdin.readline
N, M = map(int,input().split())
A = list(map(int,input().split())) # 원본배열
S = [0] * N # 합배열
C = [0] * M # 같은 나머지의 인덱스를 카운트하는 리스트
answer = 0

S[0] = A[0]
for i in range(1, N):
    S[i] = S[i - 1] + A[i] # 합배열
for i in range(0, N):
    remainder = S[i] % M
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(M):
    if C[i] > 1:
        answer += C[i] * (C[i] - 1) // 2 # combination 공식

print(answer)