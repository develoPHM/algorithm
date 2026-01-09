def solution(want, number, discount):
    from collections import Counter

    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n

    for i in range(len(discount) - 9):
        c = Counter(discount[i:i + 10])
        if c == check:
            answer += 1

    return answer

# ----------------------------------- #
def solution(want, number, discount):
    cnt = 0
    wantSum = sum(number)
    myDic = dict(zip(want, number)) # 내가 사고싶은 딕셔너리
    # 길이10짜리 초반 딕셔너리 만들기
    dic = {}
    for i in range(wantSum):
        dic[discount[i]] = dic.get(discount[i], 0) + 1

    # dic ,myDic 비교해가기
    for i in range(len(discount) - wantSum + 1):
        # (1) 현재 윈도우가 내 희망 리스트와 일치하는지 확인
        if dic == myDic:
            cnt += 1

        # (2) 다음 칸으로 이동 준비 (마지막 루프가 아니라면)
        if i + wantSum < len(discount):
            # 나가는 아이템 (i번째)
            out_item = discount[i]
            dic[out_item] -= 1
            if dic[out_item] == 0:
                del dic[out_item]  # 0이 되면 삭제해야 == 비교 가능!

            # 들어오는 아이템 (i + wantSum번째)
            in_item = discount[i + wantSum]
            dic[in_item] = dic.get(in_item, 0) + 1
    return cnt