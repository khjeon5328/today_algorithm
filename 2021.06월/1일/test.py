from itertools import combinations

for comb1 in list(combinations([(1, 0), (-1, 0), (0, 1), (0, -1)], 3)):
    for dx, dy in comb1:
        print(dx, dy)
    

print(combinations([(1, 0), (-1, 0), (0, 1), (0, -1)], 3))