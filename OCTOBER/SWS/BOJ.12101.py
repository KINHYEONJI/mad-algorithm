n, k = map(int, input().split())

lst = [1, 2, 3]
result = []

def dfs(num, Sum, n):
    global lst, result

    if Sum == n:
        result.append(num)
        return
    if Sum > n:
        return
    
    for i in lst:
        dfs(num + [i], Sum + i, n)


dfs([],0,n)
if k - 1 < len(result):
    print( '+'.join(map(str, result[k-1])))
else:
    print(-1)
