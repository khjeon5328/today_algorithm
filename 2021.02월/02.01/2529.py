import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = list(input().split())
# print(N, arr)
visited = [0] * 10

def check(num1, num2, sign):
    if sign == '>':
        if num1 > num2:
            return True
        else:
            return False
    else:
        if num1 < num2:
            return True
        else:
            return False
minV = ''
maxV = ''


def dfs(k, ans):
    global minV, maxV

    if k == N:
        if not len(minV):
            minV = ans
        else:
            maxV = ans
        return
    
    for i in range(10):
        if not visited[i] and check(int(ans[-1]), i, arr[k]):
            visited[i] = 1
            dfs(k+1, ans + str(i))
            visited[i] = 0

for i in range(10):
    visited[i] = 1
    dfs(0, f'{i}')
    visited[i] = 0

print(maxV)
print(minV)