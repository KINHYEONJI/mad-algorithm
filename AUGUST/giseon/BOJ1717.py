N,M=map(int,input().split())

def findboss(member):
    global bucket
    if bucket[member]==-1:         #-1인 경우 자기자신이 두목인 경우(여기서 0은 인덱스로 사용하기 때문에)
        return member
    ret=findboss(bucket[member])
    bucket[member]=ret
    return ret

def union(a,b):                
    global bucket
    fa,fb=findboss(a),findboss(b)
    
    if fa==fb:
        return
    bucket[fb]=fa

bucket=[-1]*(N+1)                  #a,b는 0으로 시작이 가능해 자기자신이 보스인지 0이 보스인지 구별위해 -1로 세팅
lst=[]
for i in range(M):
    lst.append(list(map(int,input().split())))

for i in range(M):
    flag,a,b=lst[i]
    if flag==1:                   #1인 경우 부모 확인 통해 집합 같은지 확인
        if findboss(a)==findboss(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)