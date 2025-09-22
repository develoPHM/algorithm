def calc(mit, jisoo):
    ans = 1
    while jisoo > 0:
        if jisoo % 2 == 1:
            ans = (ans * mit) % p
        mit = (mit * mit) % p
        jisoo //= 2
    return ans

def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i % p
    return ans


N, K = map(int, input().split())
p = 1000000007
top = factorial(N)
bottom = factorial(N - K) * factorial(K)

print(top * calc(bottom, p - 2) % p)
