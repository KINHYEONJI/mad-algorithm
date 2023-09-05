import sys
# input = sys.stdin.readline().split()
T = int(sys.stdin.readline().strip())
for _ in range(T):  # test case 반복 실행
    rd = list(sys.stdin.readline().strip())  # 함수 리스트에 넣기
    N = int(sys.stdin.readline().strip())  # 리스트 안에 정수 개수
    llst = sys.stdin.readline().strip() # 리스트 자체를 문자로 받았을 때 숫자만 리스트에 다시 넣기
    lst = []
    if N > 0: # 빈 배열이 주어진게 아니라면 받은 리스트에서 괄호 뺀 부분을 , 구분자로 lst에 넣기
        lst.extend(llst[1:-1].split(','))

    cnt_r = 0
    result = 0
    for i in rd: # 수행할 함수 만큼 반복
        if lst: # 리스트가 비어 있지 않으면
            if i == 'R':
                cnt_r += 1
            elif i == 'D':
                if cnt_r % 2 == 1: # r이 홀수 이면 pop()
                    lst.pop()
                else: # r이 짝수 이면 pop(0)
                    lst.pop(0)
        else:
            if i == 'D':
                result = 2
                break
            if i == 'R':
                result = 1

    if cnt_r % 2 == 1: # r의 총 갯수가 홀수 이면 마지막 에 한번 뒤집기
        lst.reverse()

    if result == 0: # result가 0이면, join 사용해서 리스트로 출력
        number = ','.join(lst)
        print(f'[{number}]')
    elif result == 1: # result가 1이면 [] 출력
        print([])
    elif result == 2: # result가 2이면 error 출력
        print('error')

