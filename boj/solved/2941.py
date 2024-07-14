word = input()
s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
idx = 0
while idx < len(word):
    if len(word) - 1 > idx and word[idx:idx + 2] == 'c=' or word[idx:idx + 2] == 'c-' or word[idx:idx + 2] == 'd-' or word[idx:idx + 2] == 'lj' or word[idx:idx + 2] == 'nj' or word[idx:idx + 2] == 's=' or word[idx:idx + 2] == 'z=':
        cnt += 1
        idx = idx + 2
        continue
    elif len(word) - 2 > idx and word[idx:idx + 3] == 'dz=':
        cnt += 1
        idx = idx + 3
        continue
    else:
        idx = idx + 1
        cnt += 1
print(cnt)
