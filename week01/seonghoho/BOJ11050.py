n, k = map(int, input().split())
#5C2 이면 5!을 2!(5-2)! 으로 나눈 결과값
mo = 1
ja = 1
# nCk는 n-k+1 ~ n까지 곱한 값이 분자, 
# 1~k까지 곱한 값이 분모
for i in range(n-k+1,n+1):
    ja *= i
for j in range(1,k+1):
    mo *= j

print(ja//mo)