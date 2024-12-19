def solution(wallet, bill):
    cnt = 0
    if wallet[0] < wallet[1]:
        wallet[0],wallet[1] = wallet[1], wallet[0]
    while True:
        if bill[0] < bill[1]:
            bill[0], bill[1] = bill[1], bill[0]
        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            break
        bill[0] = int(bill[0] / 2)
        cnt += 1
    return cnt