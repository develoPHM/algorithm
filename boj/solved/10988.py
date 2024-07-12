word = input()
ans = 1
for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:
        ans = 0
        break
print(ans)
