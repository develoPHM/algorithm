name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
ans = []
dic = {}
for i in range(len(name)):
    dic[name[i]] = yearning[i]
for i in range(len(photo)):
    point = 0
    for j in range(len(photo[i])):
        if photo[i][j] in dic:
            point += dic[photo[i][j]]
    ans.append(point)
print(ans)