"""
팩토리얼
5! = 5 * 4 * 3 * 2 * 1
"""


# 파라미터가 1보다 낮으면 1 리턴하고 아니면 num-1 호출해서 num과 곱하기
def factorial(num):
    if num <= 1:
        return 1

    return num * factorial(num - 1)


# 함수 호출 및 출력
N = int(input())
ans = factorial(N)
print(ans)
