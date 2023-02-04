
def fact(k):
    global n

    if k == n:
        return k
    
    return k * fact(k+1)

    

n = int(input())
if n:
    ans = fact(1)
    print(ans)
else:
    print(1)
