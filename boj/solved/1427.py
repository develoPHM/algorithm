N = int(input())
N = list(str(N))
N.sort(reverse=True)
for c in N:
    print(c,end='')
