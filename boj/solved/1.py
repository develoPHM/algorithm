MAX_PRIME = 40
prime = [True] * MAX_PRIME
prime[0] = False
prime[1] = False
for i in range(2, int(MAX_PRIME ** 0.5) + 1):
    if not prime[i]:
        continue
    for j in range(i + i, MAX_PRIME, i):
        prime[j] = False
print(prime)