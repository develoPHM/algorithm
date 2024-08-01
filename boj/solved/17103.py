import sys

input = sys.stdin.readline
MAX_PRIME = 1000001
prime = [True] * MAX_PRIME
prime[0] = False
prime[1] = False
for i in range(2, int(MAX_PRIME ** 0.5) + 1):
    if not prime[i]:
        continue
    for j in range(i + i, MAX_PRIME, i):
        prime[j] = False

T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(2, N // 2 + 1):
        if prime[i] and prime[N - i]:
            cnt += 1
            # print(i, N - i)
    print(cnt)
