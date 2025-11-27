def solution(s):
    arr = [s[0]]
    for i in range(1, len(s)):
        if len(arr) == 0:
            arr.append(s[i])
            continue
        if arr[-1] == s[i]:
            arr.pop()
        else:
            arr.append(s[i])
    if len(arr) == 0:
        return 1
    else:
        return 0

