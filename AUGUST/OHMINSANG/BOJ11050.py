'''
이항계수의 정의:
이항식을 이항 정리로 전개 했을 때 각 항의 계수이며, 주어진 크기의 순서없는 조합의 가짓수

이항식 --> 다항식

이항 정리 --> 이항식의 거듭제곱을 이항 계수를 계수로 하는 일련의 단항식들의 합으로 전개하는 정리
이항 계수 표 --> 파스칼의 삼각형이라고도 부름
nCk
7C3 --> (7 * 6 * 5)/(3 * 2)
'''
N, K = map(int, input().split())
n = 1
for i in range(N, N - K, -1):
    n *= i
# print(n)
k = 1
for j in range(K, 0, -1):
    k *= j
# print(k)
print(int(n / k))

