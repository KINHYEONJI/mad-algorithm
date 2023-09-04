import sys
input = sys.stdin.readline

def check(x,y):
    global arr  # 해당 값이 속해있는 집합의 보스를 찾는 함수
    bx, by = bossfind(x), bossfind(y)
    if bx == by:
        return 1

def bossfind(a):    # 본인의 보스가 0인 a값을 리턴해서 꺼낸다.
    global arr
    if arr[a] == -1:
        return a
    ret = bossfind(arr[a])
    arr[a] = ret
    return ret

def union(x,y):
    global arr      # 해당 값이 속해있는 집합의 보스를 찾는 함수
    bx, by = bossfind(x), bossfind(y)
    if bx == by:
        return
    arr[by] = bx    # 합집합 만드는 과정이니 해당값에 합집합의 보스를 넣어야 한다.

N,M = map(int, input().split())     # N+1개의 집합, M개의 연산 수
lst = [list(map(int, input().split())) for _ in range(M)]
# lst.sort(key=lambda x:x[0])
arr = [-1]*(N+1)     # 해당 값과 연결된 보스 저장하는 빈 배열

for i in range(M):
    if lst[i][0] == 0:      # 0일 때는 합집합 실행
        union(lst[i][1],lst[i][2])
    else:                   # 1일 때는 포함여부 확인
        if check(lst[i][1],lst[i][2]) == 1:
            print('YES')    # 합집합이면 YES 출력
        else:
            print('NO')     # 아니면 NO 출력