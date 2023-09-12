import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

start, end = 0, 0
minn = sys.maxsize

while start < N and end < N:
    ans = lst[end] - lst[start]
    if ans < M:
        end += 1
    else:
        minn = min(ans, minn)
        start += 1  # 리스트가 크기 순으로 정렬되어 있으므로, end를 옮겨 다음을 탐색할 필요가 없다.
print(minn)