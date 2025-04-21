def solution(numbers):
    arr = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] in arr:
                continue
            arr.append(numbers[i] + numbers[j])
    arr.sort()
    return arr