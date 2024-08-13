# N, M = map(int, input().split())
#
# li = []
#
#
# def f(start):
#     if len(li) == M:
#         print(*map(str, li))
#         return
#
#     for i in range(start, N + 1):
#         if len(li) > 1 and i < li[-1]:
#             continue
#         else:
#             start += 1
#             li.append(i)
#             f(start - 1)
#             li.pop()
#
#
# f(1)


N, M = map(int, input().split())
li = []

def f(start):
    if len(li) == M:
        print(*map(str, li))
        return

    for i in range(start, N + 1):
        li.append(i)
        f(i + 1)
        li.pop()
        # start += 1

f(1)
