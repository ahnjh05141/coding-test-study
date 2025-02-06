# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    if len(money) == 1:
        return money[0]

    def dp_solver(money):
        dp = [0] * len(money)
        dp[0], dp[1] = money[0], max(money[0], money[1])

        for i in range(2, len(money)):
            dp[i] = max(dp[i-1], dp[i-2] + money[i])

        return dp[-1]

    case1 = dp_solver(money[:-1])
    case2 = dp_solver(money[1:])
    
    return max(case1, case2)
