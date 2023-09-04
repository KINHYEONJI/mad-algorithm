import math
n,m = map(int,input().split())
num = n*m
def abc():
    for i in range(int(math.sqrt(num)),0,-1):
        if not num%i:
            r,a,b,c,d = 0,i,num//i,i,num//i
            while d:
                r = c%d
                c,d = d,r
            if c == n and a*b//c ==m: return print(a,b)
abc()