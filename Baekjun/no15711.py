import math

def isSosu(num):
    if num < 2: return False
    if num == 2: return True
    if num%2 == 0: return False
    if str(num)[-1] == "0": return False
    if str(num)[-1] == "5": return False
    
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num%i == 0: return False
    return True

def canSosu(a, b):
    sum = a + b
    print(sum)
    if sum%2 == 1:
        return isSosu(sum-2)
    if sum == 4: 
        return True
    
    for i in range(3, sum//2, 2):
        if isSosu(i):
            if isSosu(sum-i): return True
    return False

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if canSosu(a, b):
        print("YES")
    else:
        print("NO")

# 시간초과