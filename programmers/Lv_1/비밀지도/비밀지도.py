def solution(n, arr1, arr2):
    arr3 = [0] * n
    ans = []
    for i in range(n):
        arr3[i] = str(int(bin(arr1[i])[2:]) + int(bin(arr2[i])[2:]))
    for i in range(n):
        arr3[i] = '0' * (n - len(arr3[i])) + arr3[i]
    for i in range(n):
        a = ''
        for j in range(n):
            if arr3[i][j] == '0':
                a += ' '
            else:
                a += '#'
        ans.append(a)
    return ans