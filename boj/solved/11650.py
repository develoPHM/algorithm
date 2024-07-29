import sys
input = sys.stdin.readline
N = int(input())
li = []
for i in range(N):
    a, b = map(int, input().split())
    li.append([a, b])
li.sort(key=lambda x: x[0])
ans = [li[0]]
for i in range(1, len(li)):
    if li[i][1]