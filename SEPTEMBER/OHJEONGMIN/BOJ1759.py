def dfs(start,level):
    if level==l:
        # print(*arr)
        x,y = valid(arr)
        if x>=1 and y>=2:
            arr.sort()
            if ''.join(arr) in result:
                return
            result.append(''.join(arr))
        return
    for i in range(start,c):
    #     if used[i]==0:
    #         used[i]=1
        arr.append(lst[i])
        dfs(i+1,level+1)
            # used[i]=0
        arr.pop()
def valid(password):
    a_Sum,b_Sum =0,0
    v_lst = ['a','e','i','o','u']
    for i in password:
        if i in v_lst:
            a_Sum+=1
        else:
            b_Sum+=1
    return a_Sum,b_Sum
l,c = map(int,input().split())
lst = list(input().split())
lst.sort()
arr,result = [],[]

dfs(0,0)
result.sort()
for i in result:
    print(i)

