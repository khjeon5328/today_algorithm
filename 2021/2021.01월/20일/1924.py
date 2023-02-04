import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline
#  1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
accum = [0] * 13
for i in range(1, 13):
    if i in a:
        accum[i] = accum[i-1] + 31
    elif i in b:
        accum[i] = accum[i-1] + 30
    else:
        accum[i] = accum[i-1] + 28
# print(accum)

m, d = map(int, input().split())
num = accum[m-1] + d
num %= 7
# SUN, MON, TUE, WED, THU, FRI, SAT
if num == 1:
    print('MON')
elif num == 2:
    print('TUE')
elif num == 3:
    print('WED')
elif num == 4:
    print('THU')
elif num == 5:
    print('FRI')
elif num == 6:
    print('SAT')
elif num == 0:
    print('SUN')