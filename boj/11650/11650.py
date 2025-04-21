import sys
input = sys.stdin.readline
N = int(input())
li = []
for i in range(N):
    a, b = map(int, input().split())
    li.append([a, b])
li.sort(key=lambda x: (x[0],x[1]))
for c in li:
    print(*c)