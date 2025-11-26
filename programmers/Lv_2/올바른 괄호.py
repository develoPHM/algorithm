def solution(s):
    arr = []

    for c in s:
        if len(arr) == 0:
            arr.append(c)
            continue
        if c == ')' and arr[-1] == '(':
            arr.pop()
        else:
            arr.append(c)
    if len(arr) == 0:
        return True
    else:
        return False


print(solution('()()'))