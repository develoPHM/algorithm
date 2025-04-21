def isprime(n):
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True


def solution(n, k):
    num = ''
    ans = 0
    while n >= k:
        num += str(n % k)
        n = n // k
    num = num + str(n)
    num = num[::-1]
    arr = num.split('0')

    for i in range(len(arr)):
        if arr[i] == '':
            continue
        if isprime(int(arr[i])):
            ans += 1
    return ans
