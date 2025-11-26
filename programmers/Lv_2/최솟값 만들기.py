def solution(a, b):
    a.sort()
    b.sort(reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

print(solution([1,4,2], [5,4,4]))