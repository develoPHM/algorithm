N = int(input())
start = 1
move = 1
while start < N:
    start = start + 6 * move
    move += 1
print(move)