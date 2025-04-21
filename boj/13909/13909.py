# 'T', 'T', 'F', 'F', 'F', 'T', 'F', 'T', 'F', 'F', 'F', 'T', 'F', 'T', 'F', 'F', 'F', 'T', 'F', 'T', 'F', 'F', 'F', 'T', 'F', 'T', 'F', 'F'
n = int(input())
if n < 5:
    print(1)
    exit(0)
prime = [True] * n
prime[0] = False
prime[1] = False

for i in range(2, n + 1):
    if not prime[i]:
        continue
    for j in range(i + i, n, i):
        prime[j] = False
