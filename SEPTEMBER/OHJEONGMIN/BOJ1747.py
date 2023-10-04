from collections import deque
import math
def prime_lst(q):
    global result
    m = int(math.sqrt(q))
    for i in range(2,m+1):
        if q%i ==0:
            return False
    return True
n = input()
q = deque()
q.append(list(n))

while q:
    x = q.popleft()
    if prime_lst(int(''.join(x)))==1:
        if int(''.join(x))==1:
            print(2)
            break
        if ''.join(x) == ''.join(reversed(x)):
            print(*x,sep='')
            break
    y = int(''.join(x))+1
    q.append(list(str(y)))