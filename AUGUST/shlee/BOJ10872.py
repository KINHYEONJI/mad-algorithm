def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)  # 팩토리얼 성질( n! = n*(n-1)! ) 이용


N = int(input())
print(fact(N))
