# 자리수의 합?

# 1~9 .... 1의 자리면 cnt += 1
# 10~99 ... 10^1 이면 cnt += 2 
# 100 ~ 999 ... 10^2 이면 cnt += 3

num = int(input())
len_num = len(str(num)) # 문자열로 바꿔서 자리수 찾기


cnt = 0
for leng in range(len_num,0,-1): # 100이면 leng(10의 지수)은 3,2,1
    
    if (leng-1) <= 0: # 일의자리일 때 카운트 
        for n in range(num):
            cnt += 1
        continue      # 계산 했으니 아래 계산은 패스 
    
    # [입력받은 문자 - 입력받은 문자의 자리수(범위)] * 자리별 count
    # ex) num = 976 
    # (977(범위+1) - 10^2) * 3
    # = (977- 100) * 3
    # = 877 * 3
    # 100의 자리수(877개) 길이 2631
    debug_check = ( ((num+1) - (10 ** (leng-1))) * leng)
    cnt += debug_check # 디버그 값 확인용 변수 
    
    # 다음 자리수부터는 99 ~ 10
    # 9 ~ 1 처럼 10의 지수로 딱딱 떨어지므로
    # 10^(현 제곱)
    # 범위를 찾기위해 debug_check에 num에 1을 더했으므로
    # 중복을 막기위해 num 에는 -1 
    num = (10**(leng-1))-1


print(cnt)
    