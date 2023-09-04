N,M=map(int,input().split()) #N은 리스트개수 m은 뽑을개수 rs의 길이
rs=[0]*M
lst=list(map(int,input().split()))
lst.sort() #오름차순이니 한 번 정렬 후 진행한다
used=[0]*N

def abc(level):
    global used
    if level==M:
        print(*rs,sep=' ')
        return
    
    for i in range(N):
        if used[i]==1:continue
        used[i]=1
        rs[level]=lst[i]
        abc(level+1)
        used[i]=0

abc(0)
