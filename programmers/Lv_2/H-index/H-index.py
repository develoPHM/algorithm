# 0 1 3 5 6
def solution(citations):
    ans = 0
    citations.sort()
    n = len(citations)
    for i in range(n):
        h = n - i
        if citations[i] >= h:
            ans = h
            break

    return ans