s = input()
s = s.upper()
count = [0] * 26
for c in s:
    cur_idx = ord(c) - ord('A')
    count[cur_idx] += 1

max_idx = 0
for i in range(len(count)):
    if count[i] > count[max_idx]:
        max_idx = i

max_cnt = 0
for i in range(len(count)):
    if count[max_idx] == count[i]:
        max_cnt += 1

if max_cnt > 1:
    print('?')
else:
    print(chr(ord('A') + max_idx))
