a = int(input())
b = int(input())
c = int(input())
num = str(a * b * c)
# 17037300
ans = [0] * 10
for c in num:
    ans[int(c)] += 1
for c in ans:
    print(c)