import sys
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]  # 19x19 바둑판

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if lst[x][y] != 0:      # 0이 아닌 곳에서 시작
            focus = lst[x][y]

            for i in range(4):  # 오른쪽, 아래, 대각선 아래 두 곳 탐색
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]
                                # 범위 안에 있고, 시작점과 숫자가 같은 경우
                while 0 <= nx < 19 and 0 <= ny < 19 and lst[nx][ny] == focus:
                    cnt += 1    # cnt 더하기

                    if cnt == 5:
                        # 6개가 일치 했을 경우
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and lst[x - dx[i]][y - dy[i]] == focus:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and lst[nx + dx[i]][ny + dy[i]] == focus:
                            break
                        print(focus)    # 6개 일치 하지 않으면 출력
                        print(x + 1, y + 1)
                        sys.exit(0)     # 바로 종료 시키는 방법

                    nx += dx[i] # nx값 계속 증가시켜서 while문 벗어나기
                    ny += dy[i]

print(0)    # 오목이 없다면 0 출력