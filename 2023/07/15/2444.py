import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = 2*n -1 
# print(arr)

for i in range(1, m+1):
    # arr = [' ' for _ in range(m)]
    if i > n:
        x = 2*n-i   
    else:
        x = i
    print(' '*(n-x) +  '*'*(2*x-1))    
    # for j in range(2*x-1):
    #     arr[n+1-x+j-1] = '*'
    
