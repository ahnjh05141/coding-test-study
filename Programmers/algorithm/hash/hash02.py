# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    c = sorted(completion)
    p = sorted(participant)
    for i in range(0, len(c)):
        if c[i] != p[i]: return p[i]
    return p[-1]