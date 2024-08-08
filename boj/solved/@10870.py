# N = int(input())
#
#
# def pbo(num, cnt, a, b):
#     if cnt == num:
#         return b
#     b = a + b
#     cnt += 1
#
#     return pbo(num, cnt, b, a)
#
#
# print(pbo(N, -1, 0, 1))
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n-1) + f(n-2)