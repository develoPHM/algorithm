def solution(n):
    answer = 0
    num = str(n)
    for c in num:
        answer += int(c)

    return answer