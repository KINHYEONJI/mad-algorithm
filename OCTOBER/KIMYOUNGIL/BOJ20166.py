n,m,k = map(int,input().split())
arr = [input() for _ in range(n)]
st = [input() for _ in range(k)]

dir = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
def dfs(level,y,x,s):
    if level == 6: return
    dic[s] = dic.get(s,0) + 1
    for i in range(8):
        dy = (y + dir[i][0])%n
        dx = (x + dir[i][1])%m
        dfs(level+1,dy,dx,s+arr[dy][dx])

dic = {}
for i in range(n):
    for j in range(m):
        dfs(1,i,j,arr[i][j])

for i in range(k):
    print(dic.get(st[i],0))