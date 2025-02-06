# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    cnt = 0
    for c in s:
        if c == '(': cnt += 1
        elif c == ')': cnt -= 1
        
        if cnt<0: return False
    return cnt==0