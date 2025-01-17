from itertools import combinations
clothes = [["yellow_hat", "headgear"],
           ["green_turban", "headgear"],
           ["blue_sunglasses", "eyewear"],
           ["crow_mask", "face"], ["blue_sunglasses", "face"],]

dic = {}
li = []
ans = 0
for c in clothes:
    if c[1] in dic:
        dic[c[1]].append(c[0])
    else:
        dic[c[1]] = [c[0]]
for key, values in dic.items():
    li.append(values)