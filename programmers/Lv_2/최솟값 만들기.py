def solution(a,b):
    a.sort()
    b.sort(reverse=True)
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s