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