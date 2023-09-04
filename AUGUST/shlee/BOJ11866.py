from collections import deque

N,K = map(int,input().split())
lst = []        # 결과 출력할 리스트 생성
q = deque()
for i in range(N):
    q.append(i+1)       # 큐에 1부터 N까지 추가

while q:        # 큐에 원소가 없을 때까지 반복
    for i in range(K-1):
        now = q.popleft()   # 제거 대상 전의 원소들을 왼쪽 부터 pop
        q.append(now)       # 큐의 뒤로 재추가
    num = q.popleft()       # 원소 제거
    lst.append(num)

ret = ', '.join(map(str,lst))
print('<'+ret+'>')
