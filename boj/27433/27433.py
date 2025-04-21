import sys
sys.setrecursionlimit(10000)

N = int(input())


def ft(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * ft(num - 1)


print(ft(N))
