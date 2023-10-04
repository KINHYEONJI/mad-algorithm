N, M = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
end = 0
Sum = 0

for start in range(N):

    while Sum < M and end < N:
        Sum += lst[end]
        end += 1

    if Sum == M:
        cnt += 1
    Sum -= lst[start]

print(cnt)