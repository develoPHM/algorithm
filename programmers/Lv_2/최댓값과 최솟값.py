def solution(s):
    a = s.split(' ')
    print(a)
    arr = []
    for c in a:
        arr.append(int(c))
    return str(min(arr)) + ' ' + str(max(arr))

