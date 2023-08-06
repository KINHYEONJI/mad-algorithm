num = int(input())
def front_num(value):
    return value % 10 * 10  # 앞자리 숫자 구하기

def back_num(value):
    return (value % 10 + value // 10) % 10 # 뒷자리 숫자 구하기

cnt = 1
start_num = front_num(num) + back_num(num)
result_num = start_num
while start_num != num:
    start_num = front_num(result_num) + back_num(result_num)
    result_num = start_num
    cnt+=1
print(cnt)


