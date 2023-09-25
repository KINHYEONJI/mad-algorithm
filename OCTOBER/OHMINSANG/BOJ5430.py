from collections import deque

T = int(input())  # 테스트 케이스 입력
for _ in range(T):
    Function_lst = deque(list(input()))  # 연산 함수 입력
    n = int(input())  # 베열의 길이
    lst = list(input())  # 배열 입력

    # 입력된 리스트가 [] 일 경우 출력
    if lst == ['[', ']']:
        flag = 0
        for i in Function_lst:
            if i == 'D':    # 연산 함수에 D 발견시 error 출력 후 브레이크
                print('error')
                flag = 1
                break
        if flag == 1:
            continue
        for i in range(1):  # 연산 함수에 D 없으면 그냥 리스트 출력
            print(*lst, sep='')
        continue

    # 입력된 리스트에서 '[', ']' 제거 후 숫자형 문자만 골라서 int로 리스트에 담기
    lst.pop()
    lst.pop(0)
    str_lst = ''.join(lst)
    lst = str_lst.split(',')
    lst = list(map(int, lst))

    length = len(lst)   # 리스트 내 숫자 개수
    cnt = 0     # 연산 함수 내 R 개수
    Del = 0     # 연산 함수 내 D 개수

    while Function_lst:
        Function = Function_lst.popleft()   # 연산함수의 0번 인덱스 부터 뽑아서 확인
        if Function == 'R':
            cnt += 1
        else:
            Del += 1
            if len(lst) == 0:  # 연산함수가 D --> lst가 비어있으면 브레이크
                break
            if cnt % 2 == 0:  # 연산 함수가 D --> R 개수가 짝수면 앞에서 pop
                lst.pop(0)
            else:
                lst.pop()  # 연산 함수가 D --> R 개수가 홀수면 뒤에서 pop

    if cnt % 2 == 1:  # R 개수가 홀수면 리스트 리버스
        lst.reverse()

    if length >= Del:  # D 개수보다 초기 숫자의 개수가 더 많거나 같을 때
        print('[', end='')
        print(*lst, sep=',', end='')
        print(']')
    else:  # D 개수가 초기 숫자의 개수보다 많으면 에러
        print('error')

