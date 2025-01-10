def solution(arr):
    from math import gcd
    ans = arr[0]

    for c in arr:
        ans = ans * c // gcd(ans, c)

    return ans
