def solution(arr):
    ans = []
    ans.append(arr[0])
    for c in arr:
        if ans[-1] == c:
            continue
        else:
            ans.append(c)
    return ans