a = input()
rev_a = ''
# 인덱스 끝 문자부터 rev_a에 추가하며 단어 완성시킨다.
for i in range(len(a)):
    rev_a += a[len(a) - i - 1]
if a == rev_a:
    print(1)
else:
    print(0)