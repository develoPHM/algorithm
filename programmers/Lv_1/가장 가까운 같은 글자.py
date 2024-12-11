def solution(s):
    ans = []
    alpha = [-2] * 26
    for i in range(0, len(s)):
        if alpha[ord(s[i]) - 97] == -2:
            alpha[ord(s[i]) -97] = i
            ans.append(-1)
        else:
            ans.append(i - alpha[ord(s[i]) - 97])
            alpha[ord(s[i]) - 97] = i
    return ans