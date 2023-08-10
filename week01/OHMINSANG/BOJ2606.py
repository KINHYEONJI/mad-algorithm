"""
2606
바이러스
1. 컴퓨터 수 입력 받기.(정점의 수)
2. 연결된 컴퓨터의 쌍의 수 입력받기.(간선의 수)
3~n. 연결 정보
"""

n = int(input())
m = int(input())
lst = [[] for _ in range(n + 1)]

for i in range(m):
    s, e = map(int, input().split())
    # 양방향을 표현
    lst[s].append(e)
    # lst[e].append(s)

bucket = [0] * (n + 1)


def dfs(now):
    for i in lst[now]:
        bucket[i] += 1
        dfs(i)


dfs(1)
cnt = 0
for j in range(len(bucket)):
    if bucket[j]:
        cnt += 1
print(cnt)
