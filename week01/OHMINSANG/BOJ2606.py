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
bucket = [0] * (n + 1)
used = [0] * (n + 1)

for i in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)
    lst[e].append(s)  # 양방향 연결


def dfs_stack(start):
    # 스택 초기화 및 시작 노드 추가, 시작노드 방문 걸어놓기
    """ while 문 내용 설명
    스택에서 노드 꺼내서, 현재 노드와 연결된거 확인
    used가 0이면 1로 바꾸고 감염된 컴터 수 +1
    지금 노드에 연결된 노드 전부를 스택에 추가하고 다음 for문 실행
    stack가 다 제거되면 루프 종료
    """
    stack = [start]
    used[start] = 1
    while stack:
        now = stack.pop()
        for i in lst[now]:
            if used[i] == 0:
                used[i] = 1
                bucket[i] += 1
                stack.append(i)


used[1] = 1
dfs_stack(1)
cnt = sum(bucket)

print(cnt)
