import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(start, end):
    visited = [0] * 10001
    q = deque()
    q.append([start, 0])
    while q:
        num, depth = q.popleft()
        # 현재 숫자가 목표 숫자와 일치하면 결과 출력
        if num == end:
            print(depth)
            return

        # 각 자리 숫자를 바꾸면서 가능한 소수 찾기
        for i in range(3, -1, -1):  # 일의 자리부터 바꾸기 위해서 3, 2, 1, 0 순으로 순회 (자릿수 정하기)
            st_num = list(str(num))
            for j in range(10):     # 숫자 바꾸기
                if i == 0 and j == 0:
                    continue
                st_num[i] = str(j)
                Num = int(''.join(st_num))
                # 소수면서 방문하지 않았으면 추가
                if 1000 <= Num <= 10000 and  visited[Num] == used[Num] == 0:
                    visited[Num] = 1
                    q.append((Num, depth + 1))

    print("Impossible")


T = int(input())
used = [0] * 10001
# 에라스토테네스의 체를 이용해 소수 목록 구하고, bfs
for i in range(2, 10001):
    if used[i] == 1:
        continue
    for j in range(2 * i, 10001, i):
        used[j] = 1
for _ in range(T):
    start, end = map(int, input().split())
    bfs(start, end)
