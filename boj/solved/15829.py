L = int(input())
s = input()
ans = 0
for i in range(L):
    ans += (ord(s[i]) - ord('a') + 1) * (31 ** i)
print(ans % 1234567891)