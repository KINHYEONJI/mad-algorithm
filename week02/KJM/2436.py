'''
GCD와 LLM을 각각 최대공약수, 최소공배수로 가지고 있는 값
A,B (즉 , 우리가 찾아야하는 값)

1) A와 B는 GCD를 약수로 가지고 있으므로
A = a * GCD
B = b * GCD  (a,b는 각각 임의의 수 이다)으로 도출할 수 있다.

2) a,b를 구하기
LLM = GCD * a * b 이다.
a,b는 약수 중 최대인 GCD를 약수로 둔 값이므로 더이상 나누어질 수 없기에 서로소이고
이 서로소와 GCD를 곱한 값이 최대 공배수가 된다.

따라서 다음과 같은 식을 도출할 수 있다
LLM/GCD = a*b

3) 규칙
위 식은 서로소인 a,b를 곱했을 때 LLM/GCD가 되는 경우이다.
-> 이는 LLM/GCD의 약수 중 서로소 이면서 둘을 곱했을 때 다시 LLM/GCD가 되는 수 들이 정답

4) 서로소 찾기
유클리드 호제법을 통해 최대공약수가 1이 되는 숫자들을 찾는다

5) 합 최소 찾기
문제 조건에 따라 후보군 중 합이 최소가 되는 두 값을 출력한다.

'''
from math import sqrt

GCD,LLM = map(int,input().split())
AB = LLM//GCD # a*b = LLM/GCD

def calc(n1,n2): # 유클리드 호제법
    if n2 == 0:
        return n1
    return calc(n2, n1 % n2)

for a in range( int(sqrt(AB)),0,-1 ): # a*b의 제곱근부터 0까지
    b = int(AB/a)

    if AB % a == 0 and calc(a,b) == 1: # 약수고 서로소이다
        print(a * GCD, b * GCD) # A = a*GCD B = b*GCD
        break