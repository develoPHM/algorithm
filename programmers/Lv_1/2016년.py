def solution(a, b):
    arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = 0
    for i in range(a):
        day += arr[i]
    day += b
    return start[day % 7 - 1]