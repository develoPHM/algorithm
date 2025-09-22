clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

dic = {}
li = []
ans = 1
for c in clothes:
    if c[1] in dic:
        dic[c[1]].append(c[0])
    else:
        dic[c[1]] = [c[0]]
for c in dic:
    li.append(len(dic[c]) + 1)

for c in li:
    ans = ans * c
print(ans - 1)