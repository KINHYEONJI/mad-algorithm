#중복순열 

N,M=map(int,input().split()) #N리스트 길이 Mrs 길이
lst=list(map(int,input().split()))
rs=[0]*M
lst.sort() #오름차순이니깐 정렬

def abc(level):

    if level==M:
        print(*rs,sep=' ')
        return
    

    for i in range(N):
        rs[level]=lst[i]
        abc(level+1)

abc(0)

