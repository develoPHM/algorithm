H, M = map(int,input().split())
P = int(input())

if M + P >= 60:
    H += (M + P) // 60
    M = (M + P) % 60
else:
    M = M + P

if H >= 24:
    H %= 24

print(H, M)