import sys

input = sys.stdin.readline
MAX_PRIME = 123456 * 2 + 1
sum = [0] * MAX_PRIME
prime = [True] * MAX_PRIME
prime[0] = False
prime[1] = False
sum[2] = 1
for i in range(2, MAX_PRIME):
    if not prime[i]:
        continue
    for j in range(i + i, MAX_PRIME, i):
        prime[j] = False

for i in range(3, MAX_PRIME):
    if prime[i]:
        sum[i] = sum[i - 1] + 1
    else:
        sum[i] = sum[i - 1]

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        exit(0)
    print(sum[2 * n] - sum[n])
# import sys
#
# input = sys.stdin.readline
# MAX_PRIME = 123456 * 2 + 1
# prime = [True] * MAX_PRIME
# prime[0] = False
# prime[1] = False
# for i in range(2, int(MAX_PRIME ** 0.5) + 1):
#     if not prime[i]:
#         continue
#     for j in range(i + i, MAX_PRIME, i):
#         prime[j] = False
#
# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#         exit(0)
#     for i in range(n + 1, 2 * n + 1):
#         if prime[i]:
#             cnt += 1
#     print(cnt)
