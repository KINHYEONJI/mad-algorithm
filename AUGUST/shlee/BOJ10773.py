k = int(input())
arr = []
for i in range(k):
    num = int(input())
    if num == 0:        # 입력받은 수가 0이면
        arr.pop()       # 가장 마지막에 입력 받은 수 제거
    else:
        arr.append(num)
summ = 0
for i in range(len(arr)):
    summ += arr[i]

print(summ)