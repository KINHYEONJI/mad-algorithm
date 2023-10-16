def find(x):
    if parents[x] == -1: return x
    else:
        ret = find(parents[x])
        parents[x] = ret
        return ret

def union(a, b):
    finda, findb = find(a), find(b)
    if finda == findb: return
    else:
        parents[findb] = finda

N = int(input())  
M = int(input())  
lst = [list(map(int, input().split())) for _ in range(N)]
travel = list(map(int, input().split()))
parents = [-1] * (N+1) 

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            union(i+1, j+1)

result = set()
for i in range(M-1):
    if find(travel[i]) == find(travel[i+1]):
        result.add('YES')
    else:
        result.add('NO')

if 'NO' in result:
    print('NO')
else:
    print('YES')
