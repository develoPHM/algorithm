s = "  for the what  1what  "
s = s.lower()
a = s.split()
arr = []
for c in a:
    n = ''
    n += c[0].upper()
    n += c[1:]
    arr.append(n)
front_cnt = 0
back_cnt = 0
for c in s:
    if c ==' ':
        front_cnt += 1
    else:
        break
for i in range(len(s)):
    if s[len(s) - i - 1] == ' ':
        back_cnt += 1
    else:
        break
return front_cnt * ' ' + ' '.join(arr) + back_cnt * ' '