def should_draw(idx, size):
    size = size // 3
    if size <= idx < 2 * size:
        return False

    if size > 1:
        return should_draw(idx % size, size)

    return True


while True:
    try:
        N = int(input())
        x = 3 ** N
        line = ''
        for i in range(x):
            if should_draw(i, x):
                line += '-'
            else:
                line += ' '
        print(line)
    except:
        break
