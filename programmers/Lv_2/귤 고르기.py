k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3, 4]
dic = {}
plus= 0
cnt = 0
for c in tangerine:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
sorted_dic = dict(sorted(dic.items(),reverse=True, key=lambda item: item[1]))
print(sorted_dic)
for key, value in sorted_dic.items():
    if plus == k:
        print(cnt)
        break
    if plus + value > k:
        continue
    else:
        plus += value
        cnt += 1
