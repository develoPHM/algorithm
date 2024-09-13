li = []
li_1 = []
li_2 = []
N, M = map(int,input().split())
for i in range(N):
    li_1.append(list(map(int,input().split())))

M, K = map(int,input().split())
for i in range(M):
    li.append(list(map(int,input().split())))
for i in range(len(li)):
    li_2.append([li[i]])