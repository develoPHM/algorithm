s = input()
s = s.upper()
cnt = [0] * 26
for c in s:
    cur_idx = ord(c) - ord('A')
    cnt[cur_idx] += 1

max_idx = 0
for i in range(len(cnt)):
    if cnt[i] > cnt[max_idx]:
        max_idx = i

max_cnt = 0
for i in range(len(cnt)):
    if cnt[max_idx] == cnt[i]:
        max_cnt += 1

if max_cnt > 1:
    print('?')
else:
    print(chr(ord('A') + max_idx))
