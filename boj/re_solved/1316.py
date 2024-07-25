N = int(input())
ans = 0 + N
for i in range(N):
    s = input()
    check = []
    check.append(s[0])
    for i in range(1, len(s)):
        # 같은 단어가 나오면 패스
        if s[i] == s[i - 1]:
            continue
        # 다른 단어가 등장했을 때 이전에 등장했는지 체크하고 없으면 알파벳 추가
        if s[i] != s[i - 1] and s[i] not in check:
            check.append(s[i])
        # 다른 단어가 등장했을 때 중복된게 있으니 반복문 멈추고 개수 차감
        else:
            ans -= 1
            break
print(ans)

# 시간복잡도 O(N)