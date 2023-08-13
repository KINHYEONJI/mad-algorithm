"""
10773
제로
"""

lst = []
tc = int(input())
Sum = 0
for i in range(tc):
    num = int(input())
    # 입력받은 숫자가 0이면 lst의 마지막 인덱스 값을 Sum에서 빼고
    # lst의 마지막 인덱스 값 삭제하고 다음 루프로 진행
    if num ==0:
        Sum -=lst[-1]
        lst.pop()
        continue
    # 0이 아니면 해당 값을 lst에 입력하고 Sum에 더하기
    lst.append(num)
    Sum += num

print(Sum)
