def cal(graph):
    global li
    cal_li =[[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                cal_li[i][j] += (graph[i][k] * li[k][j]) % 1000
    return cal_li

N, B = map(int,input().split())
li = []
for i in range(N):
    li.append(list(map(int,input().split())))

for _ in range(B):
    cal(li)