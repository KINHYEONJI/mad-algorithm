#왼쪽부터 차례대로 한번씩만 침

def dfs(index):
    # print(lst)
    # print(index)
    if index ==n:
        cnt = 0
        for k in lst:
            if k[0]<=0:
                cnt+=1
        result.append(cnt)
        return

    if lst[index][0]<=0:
        dfs(index+1)
    else:
        flag = True
        for i in range(len(lst)):
            if index!=i and lst[i][0]>0 : #현재 계란, 내구도 없는 계란 말고 dfs돌리기
                flag = False
                lst[i][0] -= lst[index][1]
                lst[index][0]-=lst[i][1]
                dfs(index+1)
                lst[i][0] += lst[index][1]
                lst[index][0] += lst[i][1]
        if flag:
            dfs(n)

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
result = []
egg = []
cnt = 0
Max = 0
dfs(0)
if result:
    print(max(result))
else:
    print(0)