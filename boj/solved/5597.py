p = list(range(1,31))
# [1,2,3,4,5]
for _ in range(28):
    a = int(input())
    p.remove(a)
print(min(p))
print(max(p))