"""
요세푸스 문제()
0부터 len(n)까지, for 문 돌려서 k-1스탭씩 가서 버리고, i > len(k)일 때는 나눠서 나머지의 인덱스 번호에 해당 값 제거
"""
from collections import deque
n, k = map(int, input().split())
lst = []
for j in range(1, n + 1):
    lst.append(j)
cnt = 0
q = deque()

while len(lst) > cnt:
    for _ in range(3):
        q.append(lst)
    now = q.pop()
    print(now)
