n, m = 4, 4
section = [1,2,3,4]
cnt = 0
wall = [0] * (n + 1)
for c in section:
    wall[c] = 1
for i in range(1, n + 1):
    if wall[i] == 1 and i + m - 1 <= n:
        cnt += 1
        for j in range(i, i + m):
            wall[j] = 0
    elif wall[i] == 1 and i + m - 1 >= n:
        cnt += 1

print(cnt)