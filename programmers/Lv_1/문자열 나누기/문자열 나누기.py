def solution(s):
    s += '0'
    y_cnt = 0  
    n_cnt = 0  
    ans = 0  
    now = s[0]  

    for i in range(len(s)):
        if s[i] == '0':
            if y_cnt or n_cnt:
                ans += 1
                break
            break
        if s[i] == now:
            y_cnt += 1
        if s[i] != now:
            n_cnt += 1

        if y_cnt == n_cnt:
            ans += 1
            now = s[i + 1]
            y_cnt, n_cnt = 0, 0
    return ans