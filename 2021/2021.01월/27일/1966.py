import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
from collections import deque
for _ in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0
    flag = True
    while flag:
        if M:
            n = q.popleft()
            for i in q:
                if n < i:
                    q.append(n)
                    M -= 1
                    break
            else:
                M -= 1
                cnt += 1
        else:
            n = q.popleft()
            for i in q:
                if n < i:
                    q.append(n)
                    M = len(q)-1
                    break
            else:
                print(cnt+1)
                flag = False
