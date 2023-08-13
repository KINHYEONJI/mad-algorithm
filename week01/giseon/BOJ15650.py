
N,M=map(int,input().split()) #조합 문제이다
lst=[i for i in range(1,N+1)]
rs=[0]*M



def abc(level,start): #start를 넣어 브런치가 한 칸 씩 뒤로나와 중복되지 않는 새로운 조합 나오게 유도한다

    if  level==M:
        print(*rs,sep=' ')
        return
    
    for i in range(start,len(lst)): 
        rs[level]=lst[i]
        abc(level+1,i+1) # i+1 로 기준점이동.


abc(0,0)
