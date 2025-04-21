def fibo1(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo1(n - 1) + fibo1(n - 2)


def fibo2(n):
    li = [0, 1] + list(range(39))
    for i in range(2, 41):
        li[i] = li[i - 1] + li[i - 2]
        if li[i] == n:
            return i - 2
n = int(input())
print(fibo1(n),fibo2(fibo1(n)))
