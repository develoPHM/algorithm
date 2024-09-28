N, M = map(int, input().split())
li = []

def ans():
    if len(li) == M:
        print(*li)
        return
    for i in range(1, N + 1):
        if i in li:
            continue
        li.append(i)
        ans()
        li.pop()
ans()