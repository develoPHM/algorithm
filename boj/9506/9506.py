while True:
    num = int(input())
    arr = []
    if num == -1:
        break
    for i in range(1, num):
        if num % i == 0:
            arr.append(i)
    ans = ''
    for i in range(len(arr)):
        ans += str(arr[i]) + ' + '
    if sum(arr) == num:
        print(num, '=', ans[:-3])
    else:
        print(num, 'is NOT perfect.')

# a = ['a', 'b', 'c']
# print(' + '.join(a))
