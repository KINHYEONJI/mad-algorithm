# 1. 런타임 에러
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# n, m = map(int, input().split())
# ret = fact(n) // (fact(n - m) * fact(m))
# cnt = 0
# while ret % 10 == 0:
#     cnt += 1
#     ret //= 10
#
# print(cnt)

# # 2. 시간 초과
# def fact(n):
#     ans = 1
#     for i in range(1, n + 1):
#         ans *= i
#     return ans
#
# n, m = map(int, input().split())
# ret = fact(n) // (fact(n - m) * fact(m))
# cnt = 0
# while ret % 10 == 0:
#     cnt += 1
#     ret //= 10
#
# print(cnt)


# 3. 정답 - 2와 5의 개수 조합으로 찾기

def solve(n, r):
    cnt = 0
    while n != 0:
        n //= r
        cnt += n
    return cnt

n, m = map(int, input().split())

ret2 = solve(n, 2) - (solve(n - m, 2) + solve(m, 2))
# 분모(n!)에서 찾은 개수에서 분자((n-m)!*m!)에서 찾은 개수를 빼는 이유는, 지수의 성질을 이용한 것임.
ret5 = solve(n, 5) - (solve(n - m, 5) + solve(m, 5))
print(min(ret2, ret5))   # 2와 5가 쌍을 이뤄야 하므로 더 작은 수 만큼 쌍이 존재할 수 있음.