import sys


sys.stdin = open('input.txt')

N = int(input())

arr = [0] * sys.maxsize

C = 0
def insert(X, N, i):
    global C
    # 카운터 C값을 1 증가시킨다
    C += 1
    if X < N:
        if not arr[(i * 2) + 1]:
            arr[(i * 2) + 1] = X
            return C
        else:
            return insert(X, arr[(i * 2) + 1], (i * 2) + 1)
    else:
        if not arr[(i * 2) + 2]:
            arr[(i * 2) + 2] = X
            return C
        else:
            return insert(X, arr[(i * 2) + 2], (i * 2) + 2)

root = int(input())
arr[0] = root
print(0)
for _ in range(1, N):
    x = int(input())
    # print(x)
    res = insert(x, root, 0)
    print(res)
# print(arr)