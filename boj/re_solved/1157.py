a = input()
a = a.upper()
alpha = [0] * 26
for i in range(len(a)):
    alpha[ord(a[i]) - ord('A')] += 1
m = max(alpha)
m_idx = 0
m_cnt = 0
# 최대값을 만나면 인덱스 저장하고, 최대값 만나는 횟수 저장
for i in range(len(alpha)):
    if alpha[i] == m:
        m_idx = i
        m_cnt += 1
# 최대값이 1개 초과하면 ?, 그게 아니면 최대값 인덱스로 알파벳 찾기
if m_cnt > 1:
    print('?')
else:
    print(chr(m_idx + 65))

# 상수 시간복잡도
