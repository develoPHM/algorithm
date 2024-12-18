n, m = 8, 4
section = [2, 3, 6]
cnt = 0
wall = [0] * (n + 1)
for c in section:
    wall[c] = 1
# for i in range(n + 1):
#     if wall[i] and i + m - 1 <= n:
#         wall[i:i + m] = False
#         cnt += 1
#     elif wall[i] and i + m -1 > n:
#         cnt += 1
#         continue
print(cnt)