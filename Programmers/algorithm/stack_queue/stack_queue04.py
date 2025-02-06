# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    arr = list(enumerate(priorities))
    result = []

    while arr:
        a = arr.pop(0)
        if any(a[1] < b[1] for b in arr):
            arr.append(a)
        else:
            result.append(a)

    for i, (p, _) in enumerate(result):
        if location==p: return i+1

    return 0