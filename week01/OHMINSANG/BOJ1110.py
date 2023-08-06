num = int(input())
# 원본과 비교 할 복사본 생성
Num = num
flag = 1
loop_cnt = 0
'''
flag 값이 1이므로 항상 참이고, 원본과 복사본이 같아질때 0으로 False가 되면서
loop_cnt를 출력
'''
while flag:
    num_10 = Num // 10
    num_1 = Num % 10
    num_sum = (num_10 + num_1) % 10
    Num = (10 * num_1) + num_sum
    loop_cnt += 1
    if num == Num:
        flag = 0
        break
    else:
        continue

print(loop_cnt)
