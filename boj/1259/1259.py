while True:
    num = int(input())
    if num == 0:
        exit(0)
    num = str(num)
    reverse_num = ''
    for i in range(len(num)):
        reverse_num += num[len(num) - i - 1]
    if num == reverse_num:
        print('yes')
    else:
        print('no')