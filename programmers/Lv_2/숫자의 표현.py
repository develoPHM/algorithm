def solution(n):
    left = 1
    right = 1
    total = 1
    count = 0

    while left <= n:
        if total < n:
            right += 1
            total += right
        elif total > n:
            total -= left
            left += 1
        else:  # total == n
            count += 1
            total -= left
            left += 1
    return count