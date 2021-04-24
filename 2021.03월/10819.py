import sys

sys.stdin = open('input.txt')

# input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))
# print(arr)
ans = 0
def calc(arr):
    global ans
    hap = 0
    for i in range(N-1):
        hap += abs(arr[i] - arr[i+1])
    ans = max(ans, hap)

def comb(n, arr, visited):
    global N, nums
    if n == N:
        calc(arr)
        # print(arr)
        return 
    for i in range(N):
        if not visited[i]:
            arr.append(nums[i])
            visited[i] = 1
            comb(n + 1, arr, visited)
            visited[i] = 0
            arr.pop(-1)
comb(0, [], [0]*N)
print(ans)