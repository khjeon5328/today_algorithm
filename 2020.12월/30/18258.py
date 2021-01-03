import sys


sys.stdin = open('input.txt')

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
N = int(input())
q = deque()
for _ in range(N):
    s = sys.stdin.readline().rstrip().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)