def solution(numbers):
    answer = 45
    for c in numbers:
        answer -= c
    return answer