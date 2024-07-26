N, B = map(int, input().split())
ans = ''
num = 0
while N >= B:
    # 나머지가 10미만이면 문자열로 넣어주고 아니면 36진법 알파벳으로
    a = N % B
    if 10 <= a <= 35:
        ans += chr(a + 55)
    else:
        ans += str(a)
    N = N // B
# 반복문 종료 후 남은 N처리
if 10 <= N <= 35:
    ans += chr(N + 55)
else:
    ans += str(N)
print(ans[::-1])
# 시간복잡도 모름
