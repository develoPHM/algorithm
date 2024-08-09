def star(n):
    if n == 3:
        return ['***', '* *', '***']
    a = star(n // 3)
    li = []
    for c in a:
        li.append(c * 3)
    for c in a:
        li.append(c + ' ' * (n // 3) + c)
    for c in a:
        li.append(c * 3)

    return li


N = int(input())
print('\n'.join(star(N)))