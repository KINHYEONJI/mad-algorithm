# 조합은 n! //(n-m)!*m!
# 10을 가지려면 2와 5의 갯수를 파악하면 된다.

N, M = map(int, input().split())

def two_count(n):
    two = 0
    while n!= 0:
        n = n//2
        two += n
    return two

def five_count(n):
    five = 0
    while n!= 0:
        n=n//5
        five += n
    return five

res_two = two_count(N)-two_count(N-M)-two_count(M)
res_five = five_count(N)-five_count(N-M)-five_count(M)
print(min(res_two,res_five))

