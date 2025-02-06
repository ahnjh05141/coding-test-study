# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    a = len(nums)/2
    b = len(set(nums))
    answer = min(a,b)
    return answer