import math
def phi(x):
    result,p = x,2
    while p*p <= x:
        if x%p == 0:
            while x%p == 0: x //= p
            result -= result // p
        p += 1
    if x > 1: result -= result // x
    return result

n = int(input())
lst = []
for i in range(1,int(math.sqrt(n))+1):
    if n%i == 0:
        lst.append(i)
        lst.append(n//i)

lst.sort()
ans = -1
for i in lst:
    if i*phi(i) == n:
        ans = i
        break
print(ans)