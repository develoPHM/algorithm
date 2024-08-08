import sys
input = sys.stdin.readline
N = int(input())
li = list(map(int,input().split()))
m = max(li)
n = min(li)
print(m * n)