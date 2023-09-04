    
num = int(input())
init_num = num  # 반복문 탈출을 위한 초기값 저장 
cycle = 0
new_num = 0   

#
while True:
    # 1)어떤 숫자를 10의 자리수와 1의 자리수로 나눈다
    ten_place = num // 10
    one_place = num % 10
    
    #2) 어떤 숫자의 자리별 합을 구한다
    sum_places = ten_place + one_place
    
    if sum_places < 10: # 어떤 숫자의 합이 10 이하라면:
        num = (one_place*10) + sum_places
        cycle += 1
        
    else:  # 합이 10 이상이면:
    #3) 합의 1의자리수를 구한다
        sum_ten_place = sum_places // 10
        sum_one_place = sum_places - (sum_ten_place * 10)
    # 어떤 숫자의 1의자리가 10의자리 + 합이 1의자리가 1의자리 인 새로운 수를 만든다 
        num = one_place * 10 +  sum_one_place
        cycle += 1
    if num == init_num:
        break
print(cycle)

