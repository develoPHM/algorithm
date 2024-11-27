def solution(n):
    ans = list(map(str, str(n)))
    ans.sort()
    ans.reverse()
    return int(''.join(ans))