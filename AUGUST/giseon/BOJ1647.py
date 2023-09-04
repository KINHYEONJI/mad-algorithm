N,M=map(int,input().split())                         #노드개수,간선개수
lst=[]
for i in range(M):
    lst.append(list(map(int,input().split())))

arr=[0]*(N+2)                                        #arr 버킷 작성 노드+1개

lst.sort(key=lambda x:x[2])                          #오름차순정렬
# print(*lst)

cnt=0
sum=0

def findboss(member):                               #두목 찾는함수
    global arr
    if arr[member]==0:
        return member
    ret=findboss(arr[member])
    arr[member]=ret
    return ret

def union(a,b,c):                                   #조합함수
    global arr,cnt,sum
    fa,fb=findboss(a),findboss(b)
    if fa==fb:
        return
    cnt+=1                                          #두목이 다르다면 카운트해주고 더해주기
    sum+=c
    arr[fb]=fa
    
for i in range(len(lst)):
    a,b,c=lst[i]
    union(a,b,c)
    if cnt==N-2:                                    #제일 큰 마을 빼주니깐 접점에서 나올 수 있는 간선 N-1에 하나더 빼준다 N-2
        break
    if N==2:                                        #예외로 집이 2개인 경우 sum은 0이다.
        sum=0
        break
print(sum)
# print(i)