import sys


sys.stdin = open('input.txt')

n = int(input())
org = n
cnt = 1
while True:
    # print(n)
    a, b = divmod(n, 10)
    c = a+b
    d, e = divmod(c, 10)
    n = b*10 + e
    if n == org:
        break
    else:
        cnt += 1
    
print(cnt)