def solution(k, tangerine):
    dic = {}
    ans = 0
    for c in tangerine:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    dic = dict(sorted(dic.items(), reverse=True, key=lambda x: x[1]))
    for c in dic:
        if k <= 0:
            return ans
        k -= dic[c]
        ans += 1
    return ans


k = 2
ans = 0
tan = [1, 1, 1, 1, 2, 2, 2, 3]

table = {}

for x in tan:  # O(n)
    table[x] = table.get(x, 0) + 1

arr = sorted(table.values(), reverse=True)
print(arr)

for c in arr:
    k -= c
    ans += 1
    if k <= 0:
        break