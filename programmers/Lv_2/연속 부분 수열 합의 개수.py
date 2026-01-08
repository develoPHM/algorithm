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

# --------------------------------------- #
def solution(el):
    el_span = el * 2
    li = set()
    for length in range(1, len(el) + 1): # 수열 길이
        for start in range(0, len(el)): # 시작점
            sumNum = sum(el_span[start: start + length])
            li.add(sumNum)
    return len(li)