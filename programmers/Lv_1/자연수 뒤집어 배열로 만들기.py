def solution(n):
    arr = []
    for c in str(n)[::-1]:
        arr.append(int(c))
    return arr