import sys

sys.stdin = open('input.txt')

T = int(input())
# T = 1
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    r = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)
    rs = [r1, r2, r]
    m = max(rs)
    rs.remove(m)

    if r1 == r2 and r == 0:
        print(-1)
    elif sum(rs) < m:
        print(0)
    elif r1 + r2 == r or m == sum(rs):
        print(1)
    elif r1 + r2 > r:
        print(2) 