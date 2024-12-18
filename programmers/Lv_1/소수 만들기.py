from itertools import combinations
def solution(nums):
    arr = []
    ans = 0
    for c in combinations(nums, 3):
        arr.append(sum(c))

    for c in arr:
        cnt = 1
        for i in range(1, int(c ** 0.5) + 1):
            if c % i == 0:
                cnt += 1
        if cnt == 2:
            ans += 1
    return ans