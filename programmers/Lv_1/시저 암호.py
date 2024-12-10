def solution(s, n):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i == " ":
            result.append(" ")
        elif i.islower():
            new = lower.find(i) + n
            result.append(lower[new % 26])
        else:
            new = upper.find(i) + n
            result.append(upper[new % 26])
    return "".join(result)