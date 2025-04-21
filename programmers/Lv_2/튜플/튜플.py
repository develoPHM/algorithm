s = "{{123}}"
s = s[1: -1]
arr = []
a = []
state = True
n = ''
for i in range(len(s)):
    if s[i] == '}':
        state = False
        a.append(int(n))
        n = ''
        arr.append(a)
        a = []
        continue
    if s[i] == '{':
        state = True
        continue
    if state and s[i] == ',':
        a.append(int(n))
        n = ''
    if state and s[i].isdigit():
        n += s[i]

sorted_arr = sorted(arr, key=lambda x:len(x))
ans = []
for c in sorted_arr:
    for i in range(len(c)):
        if c[i] in ans:
            continue
        ans.append(c[i])
print(ans)