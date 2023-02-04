N  = int(input())
num = [0] * 91
num[1] = 1
if N != 1:
    for i in range(2, 91):
        num[i] = num[i-1] + num[i-2]
        if i == N:
            print(num[i])
            break
else:
    print(1)