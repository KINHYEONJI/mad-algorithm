N,M=map(int,input().split()) #중복순열문제
lst=[i for i in range(1,N+1)]
rs=[0]*M

def abc(level):
    global used
    if  level==M:
        print(*rs,sep=' ')
        return
   
    for i in range(len(lst)):
        rs[level]=lst[i]
        abc(level+1)

abc(0)
