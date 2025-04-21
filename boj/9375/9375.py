n = int(input())

for _ in range(n):
    num = int(input())
    dic = {}
    for i in range(num):
        wear = list(input().split())
        if wear[1] in dic:
            dic[wear[1]].append(wear[0])
        else:
            dic[wear[1]] = [wear[0]]

    cnt = 1

    for k in dic:
        cnt *= (len(dic[k]) + 1)
    print(cnt - 1)
