N,M,k =map(int,input().split()) #접점수 간선수 친구비용목표치

def findboss(target):
    if parent[target]==target:
        return target
    ret=findboss(parent[target])
    return ret

def union(a,b):
    fa,fb=findboss(a),findboss(b)

    if fa==fb:
        return
    
    if cost_l[fa] >cost_l[fb]:
        cost_l[fa]=0
        parent[fa]=fb
    else:
        cost_l[fb]=0
        parent[fb]=fa

cost_l=[0]+list(map(int,input().split()))
parent=[i for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    union(a,b)

result=sum(cost_l)

if result<=k:
    print(result)
else:
    print('Oh no')