li = [0] * 101
li[1] = 1
li[2] = 1
li[3] = 1
for i in range(4, 101):
    li[i] = li[i - 3] + li[i - 2]

t = int(input())
for i in range(t):
    n = int(input())
    print(li[n])
