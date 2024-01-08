import sys

sys.stdin = open('input.txt')


input = sys.stdin.readline


n, m = map(int, input().split())


mat1 = []
mat2 = []

for i in range(n*2):
    tmp = list(map(int, input().split()))
    if i < n:
        mat1.append(tmp)
    else:
        mat2.append(tmp)
# print(mat1, mat2)

for i in range(n):
    for j in range(m):
        print(mat1[i][j] + mat2[i][j], end=" ")
    print()