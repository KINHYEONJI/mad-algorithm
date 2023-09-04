N, K = map(int, input().split())

N_fac = 1
for i in range(1, N+1):
    N_fac *= i

K_fac = 1
for j in range(1,K+1):
    K_fac *= j

K_N_fac = 1
for k in range(1,N-K+1):
    K_N_fac *= k


print(N_fac // (K_fac * K_N_fac))


