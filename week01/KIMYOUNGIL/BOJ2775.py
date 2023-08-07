T = int(input())
for _ in range(T):
    k,n = [int(input()) for _ in range(2)]
    apart = list(range(1,15))
    for i in range(k):
        floor = [1]
        for j in range(1,n):
            floor.append(floor[j-1]+apart[j])
        apart = floor
    print(apart[n-1])