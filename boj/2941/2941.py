word = input()
s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
idx = 0

while idx < len(word):
    if word[idx] == 'c' and idx <= len(word) - 2 and word[idx + 1] == '=':
        count += 1
        idx += 2
        continue
    if word[idx] == 'c' and idx <= len(word) - 2 and word[idx + 1] == '-':
        count += 1
        idx += 2
        continue
    if word[idx] == 'd' and idx <= len(word) - 3 and word[idx + 1] == 'z' and word[idx + 2] == '=':
        count += 1
        idx += 3
        continue
    if word[idx] == 'd' and idx <= len(word) - 2 and word[idx + 1 ] == '-':
        count += 1
        idx += 2
        continue
    if word[idx] == 'l' and idx <= len(word) - 2 and word[idx + 1 ] == 'j':
        count += 1
        idx += 2
        continue
    if word[idx] == 'n' and idx <= len(word) - 2 and word[idx + 1 ] == 'j':
        count += 1
        idx += 2
        continue
    if word[idx] == 's' and idx <= len(word) - 2 and word[idx + 1 ] == '=':
        count += 1
        idx += 2
        continue
    if word[idx] == 'z' and idx <= len(word) - 2 and word[idx + 1 ] == '=':
        count += 1
        idx += 2
        continue
    count += 1
    idx += 1

print(count)
