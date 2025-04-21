import sys

input = sys.stdin.readline
from itertools import combinations

N = int(input())
for _ in range(N):
    # b>a
    a, b = map(int, input().split())
    up = 1
    down = 1
    for i in range(b - a + 1, b + 1):
        up *= i
    for i in range(1, a + 1):
        down *= i
    print(up // down)