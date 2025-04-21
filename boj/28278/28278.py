import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    command = list(map(int,input().split()))
    if command[0] == 1:
        arr.append(command[1])
        continue
    if command[0] == 2:
        if not arr:
            print(-1)
        else:
            print(arr.pop())
        continue
    if command[0] == 3:
        print(len(arr))
        continue
    if command[0] == 4:
        if arr:
            print(0)
        else:
            print(1)
        continue
    if command[0] == 5:
        if arr:
            print(arr[-1])
        else:
            print(-1)