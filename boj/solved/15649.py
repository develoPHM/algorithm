N, M = map(int, input().split())

li = []


def f():
    if len(li) == M:
        print(*map(str, li))
        return

    for i in range(1, N + 1):
        if i in li:
            continue
        li.append(i)
        f()
        li.pop()


f()
