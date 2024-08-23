def three(num):
    if num == 1:
        return '-'
    left = num // 3
    # middle = ' ' * (num // 3)
    right = num // 3
    return three(left) + ' ' * (num // 3) + three(right)
while True:
    try:
        N = int(input())
        print(three(3 ** N))
    except:
        break