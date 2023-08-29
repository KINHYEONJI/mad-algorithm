'''
N개의 신호등에서 고장난 곳을 used로 체크하고,
target의 범위만큼에서 used의 최소를 구해보자.
'''

N, target, gojang = map(int, input().split())
used = [0] * (N)                  # 고장난 신호등 1로 체크할 used 생성
lst = []
for i in range(gojang):             # 고장난 신호등을 1로 체크
    n = int(input())
    used[n-1] = 1

cnt = 0
for i in range(target):             # target만큼의 범위에서 고장난 갯수 세기
    if used[i]==1:
        cnt += 1
Min = 21e8                          # Min 값의 초기설정은 맨 처음 6개 신호등에서의 고장갯수
for i in range(N-target):
    if used[i] == 1:                # 뺄 값이 고장난 신호등이면 cnt-=1
        cnt-=1
    if used[i+target] == 1:         # 더할 값이 고장난 신호등이면 cnt +=1
        cnt+=1
    if Min>cnt:                     # 새로운 6개의 신호등 중 고장난 신호등 더 적으면 Min 갱신
        Min = cnt
print(Min)