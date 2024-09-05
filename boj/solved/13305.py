N = int(input())
distance = list(map(int,input().split()))
oil_price = list(map(int,input().split()))
oil_price.pop()
cost = 0
sum_distance = distance[0]
cur_price = oil_price[0]
for i in range(1, len(distance)):
    if cur_price < oil_price[i]:
        sum_distance += distance[i]
        continue
    cost += sum_distance * cur_price
    cur_price = oil_price[i]
    sum_distance = 0

print(cost)