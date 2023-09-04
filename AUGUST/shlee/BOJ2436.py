import math

def GCD(a,b):
    temp = a%b
    if temp == 0:
        return b
    else:
        return GCD(b, temp)


gcd, lcm = map(int, input().split())
ret = lcm // gcd

# 산술-기하 평균 공식에 의해 제곱근과 가까울수록 두 자연수의 합이 최소가 됨.
for a in range(int(math.sqrt(ret)), 0, -1):
    b = ret // a
    if ret % a==0 and GCD(a, b) == 1:  # 최대공약수 == 1 -> 서로소를 의미함.
        print(a * gcd, b * gcd)
        break
