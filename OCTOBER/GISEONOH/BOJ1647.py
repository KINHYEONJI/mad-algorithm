N,M=map(int,input().split()) #노드개수,간선개수
lst=[]
for i in range(M):
    lst.append(list(map(int,input().split())))

arr=[0]*(N+2)                #arr 버킷 작성 노드+1개

lst.sort(key=lambda x:x[2])
# print(*lst)

cnt=0
sum=0

def findboss(member):
    global arr
    if arr[member]==0:
        return member
    ret=findboss(arr[member])
    arr[member]=ret
    return ret

def union(a,b,c):
    global arr,cnt,sum
    fa,fb=findboss(a),findboss(b)
    if fa==fb:
        return
    cnt+=1
    sum+=c
    arr[fb]=fa
    
for i in range(len(lst)):
    a,b,c=lst[i]
    union(a,b,c)
    if cnt==N-2:
        break
    if N==2:
        sum=0
        break
print(sum)
# print(i)