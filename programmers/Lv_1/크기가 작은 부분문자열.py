def solution(t, p):
    cnt = 0
    for i in range(0, len(t)):
        if i + len(p) <= len(t):
            if int(t[i:i + len(p)]) <= int(p):
                cnt += 1
    return cnt