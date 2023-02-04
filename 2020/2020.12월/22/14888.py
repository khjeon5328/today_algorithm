import sys

sys.stdin = open('input.txt')

def calc(n, num1, num2):
    if n == 0:
        return num1 + num2
    elif n == 1:
        return num1 - num2
    elif n == 2:
        return num1 * num2
    else:
        if num1 > 0:
            return int(num1 // num2)
        else:
            return -int((abs(num1) // num2))

def dfs(n, k, v):
    global maxV, minV

    if n == k:
        if v > maxV:
            maxV = v
        
        if v < minV:
            minV = v
        return 
    
    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            nv = calc(i, v, nums[n])
            dfs(n+1, k, nv)
            oper[i] += 1



N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxV = -987654321
minV = 987654321
dfs(1, N, nums[0])
print(maxV)
print(minV)