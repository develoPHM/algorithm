import sys
input = sys.stdin.readline
N, M = map(int,input().split())
li = [0] + list(map(int,input().split()))
sum_li = [0] * (N + 1)
for i in range(1, N + 1):
    sum_li[i] = sum_li[i - 1] + li[i]
# print(sum_li)
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_li[j] - sum_li[i - 1])