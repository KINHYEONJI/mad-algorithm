N,M=map(int,input().split()) #N리스트 길이,m은 rs 길이
lst=list(map(int,input().split()))
rs=[0]*M
lst.sort()


def abc(level,start):

    if level==M:
        print(*rs,sep=' ')
        return
    

    for i in range(start,len(lst)):
        rs[level]=lst[i]
        abc(level+1,i+1)


abc(0,0)