import sys


sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

low, high = 0, max(lst)
while low <= high:
    mid = (low + high) // 2
    
    hap = 0
    for i in lst:
        if i > mid:
            hap += mid
        else:
            hap += i
    if hap <= M:
        low = mid + 1
    else:
        high = mid - 1
print(high)




