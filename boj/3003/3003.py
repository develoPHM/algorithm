white = list(map(int,input().split()))
black = [1, 1, 2, 2, 2, 8]
ans = []
for i in range(6):
    ans.append(black[i] - white[i])
print(*ans)