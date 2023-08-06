a,b = map(int,input().split())
n = int(input())
if 0< n+b <60:
    b=n+b
elif 60 <= n+b:
    a = a+((n+b)//60)
    b = n+b - 60*((n+b)//60)
    if a >= 24:
        a = a-24
print(a, b)