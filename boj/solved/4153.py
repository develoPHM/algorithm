while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break

    m = max(a,b,c)
    if (a ** 2 + b ** 2 + c ** 2) - 2 * (m ** 2) == 0:
        print('right')
    else:
        print('wrong')