a,b = map(int,input().split())
lst = []
for num in range(1,10000):
    if a%num==0 and b%num==0:
        lst.append(num)
    gcd = max(lst)
    lcm = a*b//gcd
print(gcd)
print(lcm)
