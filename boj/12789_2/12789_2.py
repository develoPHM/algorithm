N = int(input())
li = list(map(int, input().split()))
reversed_li = li[::-1]
num = 1
arr = []
wait = []
while len(reversed_li) > 0:
    if reversed_li[-1] == num:
        arr.append(reversed_li.pop())
        num += 1
        continue
    if len(wait) > 0 and wait[-1] == num:
        arr.append(wait.pop())
        num += 1
        continue
    wait.append(reversed_li.pop())

arr += wait[::-1]
check = []
for i in range(1, N + 1):
    check.append(i)
if check == arr:
    print('Nice')
else:
    print('Sad')
