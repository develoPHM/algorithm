N, M = map(int,input().split())
tree = list(map(int,input().split()))
max_tree = max(tree)

def cut(a, b):
    left, right = a, b
    ans = 0
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        for c in tree:
            if c >= mid:
                cnt += c - mid
            else:
                cnt += 0

        if cnt >= M:
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

        # print('l: ',left,'r: ',right,'m: ',mid, 'cnt: ',cnt)
    return ans

print(cut(0, max_tree))
