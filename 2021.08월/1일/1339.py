import sys

sys.stdin = open('input.txt')

n = int(input()) 
word = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(n)] 
alpha = [0] * 26

for i in range(n): 
    j = 0 
    for w in word[i][::-1]: 
        alpha[w] += (10 ** j) 
        j += 1

alpha.sort(reverse=True)
ans = 0
m = 9
for i in range(26):
    if alpha[i] == 0:
        break
    ans += alpha[i] * m
    m -= 1
print(ans)
    


