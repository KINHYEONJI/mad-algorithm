N = int(input())

if N%5 == 0:                # 5로 나누어 떨어지는 수
    result = N//5

elif N%5 ==1 or N%5 == 3:   # 나눴을 때 1,3이 남으면 나눈 몫에 +1
    result = (N//5)+1

elif N%5 ==2:               # 5로 나눈 나머지가 2인 값
    if N >=12:              # 11 이하 소수 등 예외 처리
        result = (N//5) + 2
    else:
        result = -1

elif N%5 ==4:               # 5로 나눈 나머지가 4인 값
    if N >= 9:              # 이하 나눠지지 않는 수 예외 처리
        result = (N//5) + 2
    else:
        result = -1
else:
    result = -1             # 나눠지지 않는 수는 -1

print(result)