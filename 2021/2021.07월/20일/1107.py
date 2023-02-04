import sys

sys.stdin = open('input.txt')

N = int(input())
M = int(input())
if M:
    miss = list(input())
else:
    miss = []

def check(n):
    num = list(str(n))
    for i in num:
        if i in miss:
            return False
    return True

ans = abs(100 - N)

for i in range(1000001):
    if check(i):    
        ans = min(ans, (len(str(i)) + abs(i-N)) )

print(ans)