# GCD, LCM = map(int, input().split())
#
# # LCM = DCD * A   (A = x*y)
# A = LCM // GCD
# lst = []
# for x in range(1, int(A ** (1 / 2)) + 1):
#     flag = 1
#     ans = 0
#     if A % x == 0:
#         y = A // x
#     for i in range(1, min(x,y)):
#         if x%i == 0 and y%i == 0:
#             flag = 2
#             ans = i
#         if ans > 1:
#             flag = 0
#             break
#     if flag == 2:
#         lst.append([GCD*x, GCD*y])
# print(*lst[-1])
# -------------------------위 코드는 실패


import math

"""
최대공약수 계산 함수. 이때 반환값 a가 1이면 서로소
"""


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


gcd, lcm = map(int, input().split())
divide = lcm // gcd  # (divide = A*B )

for i in range(1, math.isqrt(divide) + 1):
    if divide % i == 0:
        a, b = i, divide // i
        if get_gcd(a, b) == 1:
            A = a
            B = b

print(A * gcd, B * gcd)
