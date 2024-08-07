from collections import deque

N = int(input())
kind = list(map(int, input().split()))
start = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
A = []

dq = deque()

for i in range(len(kind)):
    if kind[i] == 1:
        continue
    dq.append(start[i])
for c in C:
    dq.appendleft(c)
    print(dq.pop(), end=' ')
