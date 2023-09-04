'''
lcm // gcd = a//gcd * b//gcd, c와 d로 칭하고, c와 d를 구해보자.
c와 d는 1.서로소이고, 2. c*d = lcm//gcd 이다.
'''

gcd, lcm = map(int, input().split())
mid = lcm // gcd
res1 = res2 = 0
Min = 21e8
a = b = 0
for i in range(1, mid **2 +1):
    a = i
    b = mid // i
    temp = 0
    while b:
        temp = a % b
        a = b
        b = temp
    if mid // i < i: break
    if mid % i == 0 and a == 1 and (mid // i) >= i and Min >= gcd * (mid // i) + gcd * i:
        Min = gcd * (mid // i) + gcd * i
        res1 = i
        res2 = mid // i

print(res1 * gcd, res2 * gcd)
