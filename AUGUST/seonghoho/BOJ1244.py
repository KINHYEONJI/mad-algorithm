switch = int( input()) #스위치 개수 입력
s_lst = list(map(int,  input().split())) #스위치 상태 입력
student = int( input()) #학생 수 입력 후 반복
for _ in range(student): 
    gender, num = map(int,  input().split()) #성별, 숫자카드 입력

    if gender == 1: #남학생일 경우
        for i in range(num-1, switch, num):
            if s_lst[i]:
                s_lst[i] = 0
            else:
                s_lst[i] = 1
    else: #여학생일 경우
        num -= 1
        left = right = num
        while left >= 0 and right < switch:
            if s_lst[left] == s_lst[right]:
                if s_lst[left]:
                    s_lst[left] = 0
                    s_lst[right] = 0
                else:
                    s_lst[left] = 1
                    s_lst[right] = 1
            else:
                break     
            left -= 1
            right += 1
            
if switch <= 20:
    print(*s_lst)
else:
    for i in range(len(s_lst)):
        print(s_lst[i], end=" ")
        if i+1 >= 20 and (i+1)%20 == 0:
            print()