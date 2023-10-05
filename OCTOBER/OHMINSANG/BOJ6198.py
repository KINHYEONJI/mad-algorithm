"""
23 / 10 / 05 알고 스터디
옥상 정원 꾸미기
"""
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
height = [int(input()) for _ in range(n)]
cnt = 0
q = []
for hi in height:
    while q and q[-1] <= hi: # 새로 들어오는 건물이 더 높아지면
        q.pop() # 가장 마지막에 들어온 거 제거
    q.append(hi)
    cnt += len(q) - 1  # 바라보고있는 자기 자신은 빼줘야해서 -1이 필요
    # print(f'{q}, cnt += {len(q) - 1}')
print(cnt)
