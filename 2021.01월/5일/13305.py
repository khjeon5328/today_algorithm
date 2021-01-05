import sys


sys.stdin = open('input.txt')

N = int(input())
road = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices[-1] = 0
# print(N, road, prices)
ans = 0
# init = prices[0] * road[0]
# ans += init

k = 0
while True:
    for i in range(k+1, N):
        if prices[i] < prices[k]:
            for j in range(k, i):
                ans += prices[k] * road[j]
            k += (i - k)
            break
    if k >= N-1:
        break
print(ans)