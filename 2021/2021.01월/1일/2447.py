import sys

sys.stdin = open('input.txt')



N = int(input())
arr = [['*'] * N for _ in range(N)]
def star(n, loc_y, loc_x):
    if n == 3:
        arr[loc_y + 1][loc_x + 1] = '1'
        return
    
    emt = n//3

    emt_loc_y = loc_y + emt
    emt_loc_x = loc_x + emt
    for y in range(emt_loc_y, emt_loc_y + emt):
        for x in range(emt_loc_x, emt_loc_x + emt):
            arr[y][x] = '1'
    # for i in range(9):
    star(emt, loc_y, loc_x)
    star(emt, loc_y + emt, loc_x)
    star(emt, loc_y + 2*emt, loc_x)
    star(emt, loc_y, loc_x + emt)
    star(emt, loc_y, loc_x + 2*emt)
    star(emt, loc_y + 2*emt, loc_x + emt)
    star(emt, loc_y + emt, loc_x + 2*emt)
    star(emt, loc_y + 2*emt, loc_x + 2*emt)

star(N, 0, 0)

for i in range(N):
    print("".join(arr[i]).replace('1', ' '))