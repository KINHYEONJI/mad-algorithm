# 우선 순위 큐
import heapq
n = int(input())
classroom  = []
for i in range(n):
    num,start,end = map(int,input().split())
    classroom.append([start,end])
classroom.sort(key=lambda x:x[0])

time =[]
heapq.heappush(time,classroom[0][1])
for i in range(1,n):
    if classroom[i][0]<time[0]: #시작시간이 끝나는 시간보다 작을 때
        heapq.heappush(time,classroom[i][1])
    else: #시작시간이 끝나는 시간보다 크거나 같을 때
        heapq.heappop(time)
        heapq.heappush(time,classroom[i][1])

print(len(time))