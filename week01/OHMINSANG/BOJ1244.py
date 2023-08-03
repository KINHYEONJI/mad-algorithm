"""
남학생은 자기 수 %2 =0 가 되는 스위치만 상태 전환
여학생은 자기 수 중심 좌우 대칭을 이루면서 커질 때까지 퍼지고, 대칭인 애들 전부 스위치 상태전환

Swt= 스위치
스위치 상태 1 --> on // 0 --> off
Students = 학생수
성별 스위치 번호( 남자 1, 여자 2)
 .      .
 .      .
 .      .
"""
"""

"""


def chg_swt(num_1):
    if swt[num_1] == 0:
        swt[num_1] = 1
    else:
        swt[num_1] = 0
    return


N = int(input())
# [5]가 들어가는 이유는 리스트의 인덱스와 스위치의 번호를 일치시켜주기위해 임의의 값을 추가함
swt = [-5] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    gender, num = map(int, input().split())
    # 남학생
    if gender == 1:
        # num부터 시작해서 N+1까지, num 간격으로
        for i in range(num, N + 1, num):
            chg_swt(i)
    # 여학생
    else:
        # 일단 여학생은 본인 번호는 무조건 바꿔야함
        chg_swt(num)
        for i in range(int(N + 0.1 / 2)):
            # 스위치 범위를 벗어낫을 때 loop 멈춤
            if num + i > N or num - i < 1:
                break
            # 대칭확인 후 스위치 상태 전환
            if swt[num - i] == swt[num + i]:
                chg_swt(num - i)
                chg_swt(num + i)
            # 대칭 깨지면 멈춤
            else:
                break

for i in range(1, N + 1):
    print(swt[i], end=' ')
    # 한 줄에 20개씩 출력 하기위한 줄바꿈
    if i % 20 == 0:
        print()
