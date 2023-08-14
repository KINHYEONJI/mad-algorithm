"""
요세푸스 문제()
0부터 len(n)까지, for 문 돌려서 k-1스탭씩 가서 버리고, i > len(k)일 때는 나눠서 나머지의 인덱스 번호에 해당 값 제거
"""
from collections import deque

n, k = map(int, input().split())
q = deque()
for j in range(1, n + 1):
    q.append(j)
lst = []

"""
q가 0이 될 때까지 무한루프 시행
k-1번동안 루프 돌리면서 맨 앞인덱스를 맨 뒤로 이동.
k번 째 될 때 .pop하고 그 값을 lst에 할당
위 과정을 반복
"""
while q:
    for i in range(k - 1):
        n = q.popleft()
        q.append(n)
    n = q.popleft()
    lst.append(n)

# f-string을 사용해서 리스트 요소만 출력 할 땐 "".join을 사용
print(f'<{", ".join(map(str, lst))}>')
