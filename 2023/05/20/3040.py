import sys


sys.stdin = open('input.txt')



input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(int(input()))

flag = True
for x in range(9):
    if flag:
        for y in range(9):
            if x != y:
                hap = 0
                ans = []
                for i in range(9):
                    if i != x and i != y:
                        hap += arr[i]
                        ans.append(arr[i])
                if hap == 100:
                    for i in range(7):
                        print(ans[i])
                    flag = False
                