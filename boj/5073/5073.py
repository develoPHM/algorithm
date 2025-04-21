while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    total = a + b + c
    m = max(a, b, c)
    if total - m <= m:
        print('Invalid')
    elif a == b and b == c and a == c:
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isosceles')
    else:
        print('Scalene')