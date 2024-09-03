def generate_cumulative_pattern(nums):
    result = []

    while len(nums) > 0:
        # 누적합 배열 생성
        cumulative_array = [sum(nums[:i + 1]) for i in range(len(nums))]
        print(cumulative_array)
        result.append(cumulative_array)
        nums.pop(0)  # 첫 번째 요소를 제거하여 다음 단계로 진행

    return result


# 초기 배열 설정
initial_array = [1, 2, 3, 4, 5]

# 패턴 생성
pattern = generate_cumulative_pattern(initial_array)

# 결과 출력
