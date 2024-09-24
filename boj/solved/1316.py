N = int(input())
count = 0

for _ in range(N):
    word = input()
    alpha = [False] * 26
    alpha[ord(word[0]) - ord('a')] = True
    for i in range(1, len(word)):
        cur_idx = ord(word[i]) - ord('a')
        if word[i] != word[i - 1] and alpha[cur_idx]:
            count -= 1
            break
        alpha[cur_idx] = True
    count += 1

print(count)