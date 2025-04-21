import sys
input = sys.stdin.readline
N = int(input())
li = []
for i in range(N):
    age, name = input().split()
    li.append([int(age), name])
li.sort(key=lambda x: x[0])
for c in li:
    print(c[0], c[1])
