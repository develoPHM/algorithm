H, M = map(int,input().split())
if M - 45 < 0:
    H -= 1
M -= 45

print(H % 24, M % 60)