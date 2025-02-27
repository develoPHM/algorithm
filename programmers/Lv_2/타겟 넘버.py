def solution(numbers, target):
    count = 0
    stack = [(0,0)]
    while stack:
        idx, total = stack.pop()
        if idx == len(numbers):
            if total == target:
                count += 1
            continue

        stack.append((idx + 1, total + numbers[idx]))
        stack.append((idx + 1, total - numbers[idx]))
    return count

