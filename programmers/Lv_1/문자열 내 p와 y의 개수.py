def solution(s):
    s = s.upper()
    cnt = [0,0]
    for c in s:
        if c == 'P':
            cnt[0] += 1
        elif c == 'Y':
            cnt[1] += 1
    if cnt[1] - cnt[0] == 0:
        return True
    else:
        return False