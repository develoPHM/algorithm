T = int(input())

for _ in range(T):
    R, S = input().split()
    str = ''
    for i in S:
        str += int(R) * i
    print(str)