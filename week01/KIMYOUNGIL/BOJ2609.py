a,b=map(int,input().split())
gcd = []
for i in range(1,max(a,b)+1):
    if (a%i == 0) and (b%i ==0):
        gcd.append(i)

gcd_max = max(gcd)
lcm_min = (a/gcd_max)*(b/gcd_max)*gcd_max

print(gcd_max)
print(int(lcm_min))
