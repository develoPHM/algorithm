def solution(arr, divisor):
    answer = []
    for c in arr:
        if c % divisor == 0:
            answer.append(c)

    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer