from collections import deque

N = int(input())
q = deque()
for i in range(N):      # 1부터 N까지 큐에 추가
    q.append(i+1)

while len(q)!=1:        # 큐에 원소가 하나남을 때까지 반복
    q.popleft()          # 맨 앞의 원소 버리기
    now = q.popleft()
    q.append(now)   # 그 다음으로 맨 앞 원소 뒤로 옮기기

print(*q)
