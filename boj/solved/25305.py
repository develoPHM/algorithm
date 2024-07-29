N, K = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
print(li[K - 1])
