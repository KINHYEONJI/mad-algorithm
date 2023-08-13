#N,M=map(int,input().split()) #N,N 받는다 n은 lst 와 가지수에 사용되고 m은 rs와 끝에 레벨설정에 사용
N,M=map(int,input().split())
lst=[i for i in range(1,N+1)]
rs=[0]*M
used=[0]*len(lst)


def abc(level):
    global used
    if  level==M:
        print(*rs,sep=' ')
        return
    
    for i in range(len(lst)):
        if used[i]==1:continue

        used[i]=1
        rs[level]=lst[i]
        abc(level+1)
        used[i]=0

abc(0)
