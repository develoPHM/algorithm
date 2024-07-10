list = []
ans = []
for i in range(0,10):
    num = int(input())
    list.append(num % 42)
for i in list:
    if i not in ans:
        ans.append(i)
print(len(ans))