# https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(0, len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i])
        days.append(day)
    
    for i in range(1, len(days)):
        if days[i] < days[i-1]: days[i] = days[i-1]
    days.append(0)
    
    for i in range(0, len(days)-1):
        if days[i] != days[i+1]: answer.append(answer.append(days.count(days[i])))
    
    return list(filter(None, answer))