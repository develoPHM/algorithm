def solution(n):
    ans = ''
    while n > 0:
        ans += str(n % 3)
        n = n // 3
    answer = 0
    ans = ans[::-1]
    for i in range(len(ans)):
        answer += (3 ** i) * int(ans[i])
    return answer