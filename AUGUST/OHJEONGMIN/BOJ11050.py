N,K = map(int,input().split())
k_factorial = 1
deno = 1
for _ in range(K): # 분자 구하기
    deno *= N
    N-=1
for _ in range(1,K+1):    # 분모 k팩토리얼 구하기
    k_factorial *= K
    K-=1

print(deno//k_factorial)