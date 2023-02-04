import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    y, x = map(int, input().split())
    arr.append([y, x])

dp = [0] * N
dp[1] = abs(arr[0][0] - arr[1][0]) + abs(arr[0][1] - arr[1][1]) 
ans = 0
for i in range(2, N):
    dp[i] = abs(arr[i-1][0] - arr[i][0]) + abs(arr[i-1][1] - arr[i][1]) 
    v = (dp[i] + dp[i-1]) - (abs(arr[i-2][0] - arr[i][0]) + abs(arr[i-2][1] - arr[i][1]) )
    # print(v)
    ans = max(ans, v)
# print(dp, ans)
print(sum(dp) - ans)