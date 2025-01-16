def solution(elements):
    arr = set()
    dp = elements[:]
    arr.update(dp)

    for i in range(1, len(elements)):
        for j in range(len(dp)):
            check = i + j
            if check < len(elements):
                dp[j] += elements[check]
            else:
                dp[j] += elements[check - len(elements)]
        arr.update(dp)

    return len(arr)