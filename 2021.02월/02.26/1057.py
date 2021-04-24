import sys


sys.stdin = open('input.txt')

N, a, b = map(int, input().split())

arr = [0] * N
arr[a-1] = 1
arr[b-1] = 1
# print(arr)
cnt = 1
def round(arr):
    global cnt
    n = len(arr)
    if n % 2:
        new_arr = [0] * (n // 2 + 1)
        for i in range(0, len(arr)-1, 2):
            if arr[i]==1 and arr[i+1] == 1:
                # print(arr)
                return 
            elif arr[i] == 0 and arr[i+1] == 0:
                new_arr[i//2] = 0
            elif arr[i] == 1 or arr[i+1] == 1:
                new_arr[i//2] = 1
        if arr[-1] == 1:
            new_arr[-1] = 1
    else:
        new_arr = [0] * (n // 2)
        for i in range(0, len(arr)-1, 2):
            if arr[i]==1 and arr[i+1] == 1:
                # print(arr)
                return 
            elif arr[i] == 0 and arr[i+1] == 0:
                new_arr[i//2] = 0
            elif arr[i] == 1 or arr[i+1] == 1:
                new_arr[i//2] = 1
    cnt += 1
    round(new_arr)
round(arr)
print(cnt)
    