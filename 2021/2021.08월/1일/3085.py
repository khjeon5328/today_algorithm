import sys


sys.stdin = open('input.txt')

N = int(input())


arr = [list(map(str, input())) for _ in range(N)]

def check(tmp):
    # print(tmp)
    length = 0
    for y in range(N):
        locV = 1
        locV2 = 1
        c = tmp[y][0]
        c2 = tmp[0][y]
        for x in range(1, N):
            if c == tmp[y][x]:
                locV += 1
                length = max(length, locV)
            else:
                c = tmp[y][x]
                locV = 1
         
            if c2 == tmp[x][y]:
                locV2 += 1
                length = max(length, locV2)
            else:
                c2 = tmp[x][y]
                locV2 = 1
    return length


ans = 1

for i in range(N):
    for j in range(N-1):
        if arr[i][j] != arr[i][j+1]:
            tmp = arr[i][j]
            arr[i][j] = arr[i][j+1]
            arr[i][j+1] = tmp
            ans = max(ans, check(arr))
            arr[i][j+1] = arr[i][j]
            arr[i][j] = tmp

        if arr[j][i] != arr[j+1][i]:
            tmp = arr[j][i]
            arr[j][i] = arr[j+1][i]
            arr[j+1][i] = tmp
            ans = max(ans, check(arr))
            arr[j+1][i] = arr[j][i]
            arr[j][i] = tmp

print(ans)