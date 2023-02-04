import sys


sys.stdin = open('input.txt')

n = int(input())
arr = [list(input()) for _ in range(n)]
# print(arr)

#C, P, Z, Y
def calc():
    maxV = 0
    for i in range(n):
        for j in range(n):
            arr[i][j]
       
        maxV = max(v, maxV)

    for j in range(n):
        c = p = z = y = 0
        for i in range(n):
            if arr[i][j] == 'C':
                c += 1
            elif arr[i][j] == 'P':
                p += 1
            elif arr[i][j] == 'Z':
                z += 1
            else:
                y += 1
        v = max(c, p, z, y)
        print(v)
        maxV = max(v, maxV)
    return maxV

print(calc())
