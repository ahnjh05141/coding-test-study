# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    types = []
    for c in clothes:
        types.append(c[1])
    
    for t in set(types):
        answer = answer * (types.count(t)+1)
    
    return answer-1