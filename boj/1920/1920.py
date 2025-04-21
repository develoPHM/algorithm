N = int(input())
N_li = list(map(int,input().split()))
M = int(input())
M_li = list(map(int,input().split()))
N_li.sort()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for c in M_li:
    print(binary_search(N_li, c))
