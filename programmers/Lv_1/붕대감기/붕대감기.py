def solution(bandage, health, attacks):
    max_health = health
    count = bandage[0]
    heal = bandage[1]
    plus = bandage[2]
    atk = 0
    check = 1

    for i in range(1, attacks[-1][0] + 1):
        if attacks[atk][0] == i:
            health -= attacks[atk][1] # 맞음
            check = 0 # 맞으면 연속 초기화
            atk += 1
            if health <= 0:
                health = -1
                break
            continue

        health += heal  # 그냥 회복
        check += 1

        if check == count:
            health += plus # 연속 달성해서 추가 힐
            check = 0 # 연속 성공 후 연속 초기화

        if health > max_health:
            health = max_health

        elif health <= 0:
            health = -1
            break
    return health