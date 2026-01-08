def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n - 1] % 1234567
#--------------#
def solution(n):
    if n < 3:
        return n
    arr = [0] * 2001
    arr[0] = 0
    arr[1] = 1
    arr[2] = 2
    for i in range(3, len(arr)):
        arr[i] = (arr[i - 2] + arr[i - 1]) % 1234567
    return arr[n]
