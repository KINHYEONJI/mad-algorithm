T=int(input())                      #테스트 케이스 개수
from collections import deque
for tc in range(T):
    str=input()
    # print(str)
    N=int(input())
    lst=input()
    q=deque(lst[1:-1].split(','))    #슬라이싱 아무것도 없는 경우 [''] 0아 아닌 공백들어간다 주의
    # print(q)                       #슬라이싱은 o(n)속도이니 pop() o(1) 사용
    cnt=0                            #r을 수치로 기억해두어 마지막에 연산 
    flag=0
    for i in range(len(str)):
        if str[i]=='R':
            cnt+=1
        elif str[i]=='D':   
            if not q or q[0]=='':   #배열 비어있으면 error flag on
                flag=1
                break
            if cnt%2==1:            #r의 홀짝에 따라 pop popleft 구분
                q.pop()
            else:
                q.popleft()
    if flag==1:
        print('error')
    else:
            if cnt%2==1:
                q.reverse()
                print('['+','.join(q)+']')  #문자열을 합쳐주는 조인을 이용해 출력 및 문자열 + 사용 으로 붙여주기
            elif cnt%2==0:
                print('['+','.join(q)+']')