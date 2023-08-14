from collections import deque

N, K = map(int, input().split()) # 1~N 들어간 배열, K 번째 수마다 pop

#1~N 들어간 배열 생성
lst = []
for i in range(1, N+1):
    lst.append(i)

result = deque(lst)                 # lst를 deque 배열인 result로 정의
new_lst = []
while N-len(new_lst)>0:             # result배열에 숫자가 남아있으면 반복,
    if N-len(new_lst) >1:           # deque로 정의된 리스트는 부등호처리가 불가하다. 

        for i in range(K-1):        # K번째 수를 제거하기 때문에 K-1번 왼쪽 수를 오른쪽으로 보낸다.
            a = result.popleft()    
            result.append(a)

    num = result.popleft()          # result배열의 0번째 문자를 pop한다. 
    new_lst.append(num)             # pop한 문자열 num을 new_lst에 담는 과정을 반복!


result1 = []
for i in new_lst:
    result1.append(str(i))
result2 = ', '.join(result1)
print('<'+result2+'>')              # <1, 2, 3, 4, 5> 형식을 두 가지로 구현함

# print(f'<',end='')
# for i in range(len(new_lst)-1):
#     print(f'{new_lst[i]}, ', end='')
# print(f'{new_lst[-1]}>',end='')