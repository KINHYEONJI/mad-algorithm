"""
23 / 10 / 11 알고 스터디
강의실
"""
import sys, heapq
def input(): return sys.stdin.readline().rstrip()


n = int(input())
n_s_e = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
hq, cnt = [], 0

for num, s, e in n_s_e:
    while hq and hq[0] <= s:    # 힙큐의 0번 인덱스(끝나는시간)보다 이번 강의 시작 시간이 클 때
        heapq.heappop(hq)       # 0번 인덱스 제거  

    heapq.heappush(hq, e)       # 이번타임 끝나는 시간 우선순위 큐에 푸시
    cnt = max(cnt, len(hq))     # 맥스값 비교
print(cnt)
