def dfs(x,y,z,check):
    global ans
    if y > 3: return

    if x == 7:
        check.sort()
        check = tuple(check)
        ans.add(check)
        return

    for i in range(25):
        a,b = lst[i][0],lst[i][1]
        c = dic[f'{a,b}']
        if c not in check:
            flag = 0
            for k in z:
                if abs(a-k[0]) + abs(b-k[1]) == 1:
                    flag = 1
                    break
            if flag:
                if arr[a][b] == 'S':
                    dfs(x+1,y,z+[[a,b]],check+[c])
                elif arr[a][b] == 'Y':
                    dfs(x+1,y+1,z+[[a,b]],check+[c])

arr = [list(input()) for _ in range(5)]
lst = []
dic = {}
num = 0
for i in range(5):
    for j in range(5):
        lst.append([i,j])
        dic[f'{i,j}'] = num
        num += 1

ans = set()
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            n = dic[f'{i,j}']
            dfs(1,0,[[i,j]],[n])
            arr[i][j] = '.'
print(len(ans))