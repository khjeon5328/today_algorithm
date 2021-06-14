import sys


sys.stdin = open('input.txt')

N = int(input())

ans = 0
maxV = 0
def comb(lst, n, visited, hap, person):
    global maxV, ans

    if n == 3:
        hap %= 10
        if hap >= maxV:
            # print(hap, person, visited)
            ans = person
            maxV = hap
        return
    
    for i in range(5):
        if not visited[i]:
            visited[i] = 1
            comb(lst, n+1, visited, hap + lst[i], person)
            visited[i] = 0

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    comb(tmp, 0, [0]*5, 0, i)

print(ans)
