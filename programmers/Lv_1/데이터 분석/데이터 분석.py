def solution(data, ext, val_ext, sort_by):
    ans = []
    dic = { 'code': 0,
            'date': 1,
            'maximum': 2,
            'remain': 3}
    a = dic[ext]
    for i in range(len(data)):
        if data[i][a] < val_ext:
            ans.append(data[i])

    ans.sort(key=lambda x: x[dic[sort_by]])
    return ans
