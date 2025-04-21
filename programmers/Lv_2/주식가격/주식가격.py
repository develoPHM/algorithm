def solution(prices):
    n = len(prices)
    answer = [0] * n  # 결과 리스트
    stack = []  # 가격이 떨어지지 않은 인덱스를 저장할 스택

    for i, price in enumerate(prices):
        # 가격이 떨어졌다면 스택에서 빼고 유지 시간 계산
        while stack and prices[stack[-1]] > price:
            past = stack.pop()
            answer[past] = i - past
        stack.append(i)  # 현재 인덱스 저장

    # 끝까지 가격이 떨어지지 않은 경우 처리
    while stack:
        past = stack.pop()
        answer[past] = n - 1 - past

    return answer