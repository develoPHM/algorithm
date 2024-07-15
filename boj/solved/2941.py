word = input()
s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
idx = 0

while idx < len(word):
    if word[idx] == 'c' and idx <= len(word) - 2 and word[idx + 1] == '=':
        cnt += 1
        idx += 2
        continue
    if word[idx] == 'c' and idx <= len(word) - 2 and word[idx + 1] == '-':
        cnt += 1
        idx += 2
        continue
    if word[idx] == 'd' and idx <= len(word) - 3 and word[idx + 1] == 'z' and word[idx + 2] == '=':
        cnt += 1
        idx += 3
        continue
    if word[idx] == 'd' and idx <= len(word) - 2 and word[idx + 1 ] == '-':
        cnt += 1
        idx += 2
        continue
    if word[idx] == 'l' and idx <= len(word) - 2 and word[idx + 1 ] == 'j':
        cnt += 1
        idx += 2
        continue
    if word[idx] == 'n' and idx <= len(word) - 2 and word[idx + 1 ] == 'j':
        cnt += 1
        idx += 2
        continue
    if word[idx] == 's' and idx <= len(word) - 2 and word[idx + 1 ] == '=':
        cnt += 1
        idx += 2
        continue
    if word[idx] == 'z' and idx <= len(word) - 2 and word[idx + 1 ] == '=':
        cnt += 1
        idx += 2
        continue
    cnt += 1
    idx += 1

print(cnt)
