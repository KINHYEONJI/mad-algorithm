len_switch = int(input())
switches = list(map(int, input().split()))
quantity_student = int(input())
switches.insert(0, 0) # 스위치 번호가 1부터 시작하니까 인덱스랑 맞추기 위해 맨 앞에 값 추가 

for _ in range(quantity_student):
    gender, num = map(int, input().split())

    if gender == 1:  # 남학생이면
        for k in range(num, len_switch + 1, num): # num의 배수씩 순회해서
            switches[k] = abs(switches[k] - 1)  # 1이면 0 , 0이면 1로 스위치 전환 

    elif gender == 2:  # 여학생이면
        switches[num] = abs(switches[num] - 1)  # 일단 입력 받은 번호 스위치 전환 

        i = 0 
        while num - i > 0 and num + i <= len_switch:    # 인덱스가 배열 길이 안넘게 제한
            if switches[num - i] != switches[num + i]:  # num을 기준으로 양 옆이 대칭이 아니면 반복문 탈출 
                break
            # 대칭이면 각 대칭값 상태변경
            switches[num - i] = abs(switches[num - i] - 1)  
            switches[num + i] = abs(switches[num + i] - 1)
            i += 1 # 옆칸도 대칭이면 계속 반복

# 스위치 상태 20개씩 출력 
for i in range(1, len_switch + 1):
    print(switches[i], end=' ')
    if i % 20 == 0 or i == len_switch:
        print()



# 8월 2일 수정 전 

# len_switch = int(input())
# switches = list(map(int,input().split()))
# quantity_student = int(input())
# switches.insert(0,0) 

# for _ in range(quantity_student):
#     gender, num = input().split()
#     gender = int(gender)
#     num = int(num)

#     if gender == 1: # 남학생이면

#         for k in range(num, len_switch):
#             if k % num == 0:
#                 switches[k] = abs( switches[k] - 1 ) # switch가 0이면 1 , 1이면 0으로 바꾸는 코드
    
                
#     elif gender == 2: # 여학생이면
        
#         i = 0 # 범위 인덱스용 변수 
#         switches[num] = abs(switches[num] - 1) # 일단 받은 번호에 해당하는 스위치 상태바꿈
#         while True:
            
#             if (switches[num-1-i]) - (switches[num+1+i]) != 0: # num 양옆이 대칭이 아니면
#                 break            # 반복문 탈출 -> 대칭이면 계속 반복
#             if (num-1-i) < 0 or (num+1+i) > len_switch:
#                 break
#             switches[num-1-i] = abs ( switches[num-1-i] - 1 )
#             switches[num+1+i] = abs ( switches[num+1+i] - 1 )
#             i += 1
            

# print(*switches[1:])