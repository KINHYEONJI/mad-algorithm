import sys
input = sys.stdin.readline
def dfs(level):
    global n,p,q
    if level<1:
        return 1
    elif level in lst:
        return lst[level]
    lst[level] = dfs(level//p)+dfs(level//q)
    return lst[level]

n,p,q = map(int,input().split())
lst = {}
print(dfs(n))
