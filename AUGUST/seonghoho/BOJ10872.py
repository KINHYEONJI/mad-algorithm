def abc(num, n, ret):       # 1에서 n까지 곱할 함수
    if num == n:            # 재귀함수로 num이 n까지 갈 경우
        ret *= num          # return 전 해당 재귀의 num 곱하기
        print(ret)          
        return 
    elif n == 0:            # 입력받은 n이 0일 경우 - 예외처리
        print(1)
        return 
    # ret *= num
    # num += 1
    abc(num+1, n, ret*num)  # 다음 수를 num+1로 받는 재귀로 들어가기

n = int(input())            # n 입력
abc(1, n, 1)
