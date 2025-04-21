import sys

N, M = map(int, input().split())

num_dict = {}
name_dict = {}
for i in range(N):
    a = str(input()).strip()
    num_dict[i + 1] = a
    name_dict[a] = i + 1

for _ in range(M):
    a = str(input()).strip()
    if a.isnumeric():
        print(num_dict[int(a)])
    else:
        print(name_dict[a])
