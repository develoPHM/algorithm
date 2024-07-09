H, M = map(int,input().split())
T = int(input())

if M + T >= 60:
    H += (M + T) // 60
    M = (M + T) % 60
else:
    M = M + T

if H >= 24:
    H %= 24

print(H, M)