import math
import sys

input = sys.stdin.readline

N = int(input())
li = []
cnt = 0
for i in range(N):
    li.append(int(input()))

total_gcd = li[1] - li[0]
for i in range(1, len(li)):
    total_gcd = math.gcd(total_gcd, li[i] - li[i - 1])
tree = (li[-1] - li[0]) // total_gcd
tree = tree - len(li) + 1
print(tree)