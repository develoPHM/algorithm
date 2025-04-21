N = int(input())
li = list(map(int,input().split()))
T, P = map(int,input().split())
num = 0
def t_shirt (size, bundle):
    if size % bundle == 0:
        return size // bundle
    else:
        return size // bundle + 1

for i in range(6):
    num += t_shirt(li[i], T)

print(num)
print(N // P, N % P)