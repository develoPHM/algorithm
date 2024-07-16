N = int(input())
max_x = 0
max_y = 0
point = []
cnt = 0
for _ in range(N):
    x, y = map(int,input().split())
    point.append([y,x])
    if x >= max_x:
        max_x = x
    if y > max_y:
        max_y = y
max_x += 10
max_y += 10
graph = [[0] * max_x for _ in range(max_y)]
for p in point:
    for i in range(p[0],p[0] + 10):
        for j in range(p[1], p[1] + 10):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
print(cnt)
# for i in graph[::-1]:
#     print(i)