tc = int(input()) # 입력할 숫자의 갯수

total = []                      # 입력한 숫자를 넣을 리스트
cnt = 0                         # 리스트에 들어간 문자의 갯수

for i in range(tc):             # tc만큼 반복 작업
    num = int(input())          

    if num != 0:                #0이 아니면 리스트에 문자 넣음
        total.append(num)
        cnt += 1                # 리스트에 문자 갯수 추가
    elif num == 0 and cnt > 0:  # 리스트에 문자가 있으면 0입력시 pop 실행
        total.pop()
        cnt -= 1
    else:
        continue                
        
Sum = 0
for i in range(len(total)):     # 입력받은 숫자 더해서 출력
    Sum += total[i]

print(Sum)