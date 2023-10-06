l,c = map(int,input().split())
arr = input().split()
arr.sort()

m = []
j = []
for i in arr:
    if i in ['a','e','i','o','u']:
        m.append(i)
    else:
        j.append(i)

path = [""]*l
def dfs(x,y):
    if x == l:
        cnt_m = 0
        cnt_j = 0
        for i in path:
            if i in ['a','e','i','o','u']:
                cnt_m +=1
            else:
                cnt_j += 1
        if cnt_m >= 1 and cnt_j >= 2:
            print(*path,sep="")
        return
    
    for i in range(y,c):
        path[x] = arr[i]
        dfs(x+1,i+1)

dfs(0,0)