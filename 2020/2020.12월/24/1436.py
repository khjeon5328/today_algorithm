import sys


sys.stdin = open('input.txt')

N = int(input())

num = 666

visited = [0] * N
visited[0] = 666

def check(num):
    
    cnt = 0
    while num:
        a, b = divmod(num, 10)
        if b == 6:
            cnt += 1
        else:
            cnt = 0
        num = a

        if cnt == 3:
            return True
    return False
    
i = 1
while not visited[N-1]:
    num += 1
    if check(num):
        visited[i] = num
        i += 1
print(visited[N-1])
