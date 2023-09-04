import math
def gcd(a,b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a

n,m = map(int,input().split())

mul = n*m
for i in range(int(math.sqrt(mul)),0,-1):
    if mul%i ==0 and gcd(i,mul//i)==n: #최소공배수와 최대공약수의 곱의 루트를 씌웠을 때의 값에서 부터 값 찾기 시작
        result = i                      # 두 수의 최대 공약수가 n일때만 조건 들어감
        break
print(result,mul//result)