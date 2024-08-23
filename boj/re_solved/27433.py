import sys
sys.setrecursionlimit(10000)

N = int(input())

def f(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * f(num - 1)
print(f(N))