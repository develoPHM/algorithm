K, N = map(int, input().split())
li = []
for _ in range(K):
    li.append(int(input()))
li.sort()


def binary_search(a, b):
    left, right = a, b
    ans = 0
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        for c in li:
            cnt += c // mid
        if cnt >= N:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


print(binary_search(1, max(li)))
