N, B = map(int, input().split())
# N = N[::-1]
ans = ''
num = 0
while N >= B:
    plus = N % B
    if 10 <= plus <=35:
        ans += chr(plus + 55)
    else:
        ans += str(plus)
    N = N // B
    # print('N:',N,'plus',plus)
if 10 <= N <= 35:
    ans += chr(N + 55)
else:
    ans += str(N)

print(ans[::-1])