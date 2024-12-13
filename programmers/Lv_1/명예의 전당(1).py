def solution(k, score):
    arr = []
    ans = []
    for c in score:
        if len(arr) < k:
            arr.append(c)
            ans.append(min(arr))
            continue
        arr.sort(reverse=True)
        if c > arr[-1]:
            arr.pop()
            arr.append(c)
        ans.append(min(arr))
    return ans