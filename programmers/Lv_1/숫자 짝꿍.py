def solution(X, Y):
    result = ''
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for c in X:
        value = int(c)
        a[value] += 1

    for c in Y:
        value = int(c)
        b[value] += 1

    for c in range(9, -1, -1):
        value = str(c) * min(a[c], b[c])
        result += value

    if len(result) == 0:
        return '-1'
    if result[0] == '0':
        return '0'

    return result
