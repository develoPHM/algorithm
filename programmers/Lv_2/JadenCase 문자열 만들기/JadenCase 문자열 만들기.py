def solution(s):
    s = s.lower()

    cnt = 0
    ans = ''
    for i in range(len(s)):
        if s[i] == ' ':
            cnt += 1
            continue
        if s[i] != ' ':
            ans += cnt * ' '
            cnt = 0
            if len(ans) == 0 or ans[-1] == ' ':
                ans += s[i].upper()
            else:
                ans += s[i]
    back = 0
    for i in range(len(s)):
        if s[len(s) - i - 1] == ' ':
            back += 1
        else:
            break

    ans += back * ' '
    return ans