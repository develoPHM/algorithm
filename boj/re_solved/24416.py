N = int(input())

li = [0,1] + list(range(39))
for i in range(2, 41):
    li[i] = li[i-1] + li[i-2]

print(li[N], N - 2)
