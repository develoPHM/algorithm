A, B, C = map(int,input().split())
bin_num = ''
ans = 1
while B > 0:
    binary = str(B % 2)
    bin_num += binary
    B = B // 2

for i in range(len(bin_num)):
    if int(bin_num[i]) == 0:
        continue
    else:
        ans *= A ** (2 ** i)
print(ans % C)