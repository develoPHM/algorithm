N, M = map(int,input().split())
li = []
def f(start):
    if len(li) == M:
        print(*li)
        return
    for i in range(start, N + 1):
        li.append(i)
        f(i + 1)
        li.pop()


f(1)