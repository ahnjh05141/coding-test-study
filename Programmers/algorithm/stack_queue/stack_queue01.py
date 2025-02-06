# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0:
            answer.append(a)
        elif a != answer[-1]:
            answer.append(a)
    return answer