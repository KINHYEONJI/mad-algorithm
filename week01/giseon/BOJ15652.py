
N,M=map(int,input().split()) #조합 문제이다
lst=[i for i in range(1,N+1)]
rs=[0]*M



def abc(level,start): #기준점을 브랜치 기준으로 잡아두어 뒤에 브런치로 갈수록 좁아지게 설정

    if  level==M:
        print(*rs,sep=' ')
        return
    
    for i in range(start,len(lst)): 
        rs[level]=lst[i]
        abc(level+1,i) # i 로 기준점이동.


abc(0,0)
