arr = []
ans = ''
max_len = 0
for _ in range(5):
    arr.append(input())
for s in arr:
    if len(s) >= max_len:
        max_len = len(s)
for i in range(len(arr)):
    if len(arr[i]) < max_len:
        arr[i] += ' ' * (max_len - len(arr[i]))

for i in range(max_len):
    for j in range(5):
        if arr[j][i] == ' ':
            continue
        else:
            ans += arr[j][i]
print(ans)