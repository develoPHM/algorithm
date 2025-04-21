n = int(input())
li = list(map(int, input().split()))

li.sort()
check = 2e9
idx = [0, 0]

l, r = 0, n - 1
while l < r:
    current_sum = li[l] + li[r]
    if abs(current_sum) < check:
        check = abs(current_sum)
        idx = [li[l], li[r]]

    # 합이 음수면 l을 증가, 양수면 r을 감소
    if current_sum < 0:
        l += 1
    elif current_sum > 0:
        r -= 1
    else:
        break  # current_sum == 0인 경우 최적이므로 종료
idx.sort()
print(idx[0], idx[1])