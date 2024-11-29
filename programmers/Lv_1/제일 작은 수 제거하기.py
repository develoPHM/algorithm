def solution(arr):
    ans = []
    min_num = min(arr)
    for c in arr:
        if c == min_num:
            continue
        ans.append(c)
    if len(ans) <= 1:
        return [-1]
    else:
        return ans