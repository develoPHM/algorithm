def solution(number, limit, power):
    weapon = []
    for i in range(1, number + 1):
        nums = []
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                nums.append(j)
                nums.append(i // j)
        num = len(set(nums))
        if num > limit:
            weapon.append(power)
        else:
            weapon.append(num)
    ans = sum(weapon)
    return ans