N, B = input().split()
N = N[::-1]
num = 0
for i in range(len(N)):
    if '0' <= N[i] <= '9':
        num += int(N[i]) * (int(B) ** i)
    else:
        num += (ord(N[i]) - 55) * (int(B) ** i)
print(num)

