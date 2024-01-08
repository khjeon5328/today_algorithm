import sys

sys.stdin = open('input.txt')

arr = []
hap = 0
for i in range(5):
    tmp = int(input())
    hap += tmp
    arr.append(tmp)
print(hap//5)

arr.sort()
print(arr[2])