from collections import deque

lst = deque()               # deque 사용해서 queue 사용
n = int(input())    
for i in range(1,n+1):      # 1에서 입력받은 n까지의 수가 담긴 lst 생성
    lst.append(i)           

while len(lst)>1:           # lst 길이가 1자리가 될 때까지 반복
    lst.popleft()           # 맨 왼쪽 수 popleft로 제거
    num = lst.popleft()     # 왼쪽에서 두 번째 수 num에 담아서
    lst.append(num)         # lst의 오른쪽에 더하기

print(*lst)                 # lst에 남은 한 숫자 출력
