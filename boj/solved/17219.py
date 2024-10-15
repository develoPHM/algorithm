N, K = map(int,input().split())
dic = {}
for _ in range(N):
    p = input()
    a, b = p.split(' ')
    dic[a] = b

for _ in range(K):
    find = input()
    print(dic[find])