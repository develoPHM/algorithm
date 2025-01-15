# 초기 값
initial_price = 400_000_000  # 4억
annual_increase_rate = 0.05  # 연간 5% 증가
years = 2  # 2년

# 각 연도 가격 계산
prices = [initial_price]
for _ in range(years):
    new_price = prices[-1] * (1 + annual_increase_rate)
    prices.append(new_price)

print(prices)