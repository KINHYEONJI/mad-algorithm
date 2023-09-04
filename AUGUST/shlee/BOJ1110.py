N = int(input())

a = N // 10  # 십의 자리
b = N % 10  # 일의 자리

count = 0       # 사이클 길이 초기값
while True:
    # 십의 자리 -> 원래의 일의 자리 , 일의 자리 -> 두 수의 합의 일의 자리
    a, b = b, (a + b) % 10      
    if (a == N // 10) and (b == N % 10):    # 초기 값으로 돌아오면 반복문 종료
        count += 1
        break
    count += 1      # 반복 사이클 길이 구하기

print(count)