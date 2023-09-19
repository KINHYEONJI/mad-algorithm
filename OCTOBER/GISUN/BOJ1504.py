import heapq
n,m=map(int,input().split())
inf=int(21e8)

def dijstra(start,end):
    result=[inf]*(n+1)
    heap_lst=[]
    heapq.heappush(heap_lst,[0,start])                  #값과 위치 넣어주기
    result[start]=0
    while heap_lst:
        ps,w=heapq.heappop(heap_lst)
        if ps>result[w]:continue                        #조금 헷갈렷음(최소 부터넣으니 뒤에 낮은 기대치 값 컨티뉴)
        for i in arr[w]:
            cost=ps+i[1]                                 #조금 헷갈렸음(경유지를 통해 타겟에 들어가는 새로운값 변수 생성)
            if cost<result[i[0]]:
                result[i[0]]=cost
                heapq.heappush(heap_lst,[cost,i[0]])    # 경유지까지의 값과 경유지 인덱스 추가
    return result[end]   

    


#인접리스트제작
arr=[[]for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])

target_1,target_2=map(int,input().split())

rs_1=dijstra(1,target_1)+dijstra(target_1,target_2)+dijstra(target_2,n)
rs_2=dijstra(1,target_2)+dijstra(target_2,target_1)+dijstra(target_1,n)
if min(rs_1,rs_2)>21e8:
    print(-1)
else: print(min(rs_1,rs_2))

