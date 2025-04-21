# def solution(phone_book):
#     N = len(phone_book)
#     li = sorted(phone_book)
#     for i in range(N - 1):
#         length = len(li[i])
#         if li[i] in li[i + 1][0:length]:
#             return False
#     return True

def solution(phone_book):
    answer = True
    dic = {}
    for c in phone_book:
        dic[c] = 1
    for c in phone_book:
        s = ""
        for number in c:
            s += number
            if s in dic and s != c:
                answer = False
    return answer