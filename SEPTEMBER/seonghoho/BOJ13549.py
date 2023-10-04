from collections import deque
import sys

# N이 M이 될 때까지 걸을 때의 cnt 수
N,K = map(int, sys.stdin.readline().split())
def bfs(n,cnt): # N의 값과 cnt 초기화
    q = deque() # deque 생성
    q.append([n,cnt])   # 두 개 같이 받기
    Max = 100000    # N이 갈 수 있는 최대 지점 Max로 지정
    used = [0]*100001   # 최대 지점만큼 used 배열 생성
    while q:
        now, cnt = q.popleft()  # bfs 방식으로 앞에서 꺼내기
        if now == K:    # 갱신된 N값이 K에 도달하면
            print(cnt)  # cnt 출력하고 break
            break

        for i in (now*2, now-1, now+1): # 순간이동, 걷기를 순차적으로 실행
            if 0<=i<=Max and used[i]==0: # now가 다음에 갈 i 값의 범위 확인,
                if i == now*2:  # used 0이면 실행
                        used[i]= 1 # 사용 체크 후 append
                        q.append([i, cnt])  # 순간이동이면 cnt 그대로

                else:
                    used[i] = 1
                    q.append([i,cnt+1]) # 순간이동 아니면 cnt +=1


bfs(N,0)