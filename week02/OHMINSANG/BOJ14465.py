n, k, b = map(int, input().split())
lst = []
# 0 부터 n까지 n개의 인덱스 생성
for i in range(n):
    lst.append(i)

# 입력받은 값의 인덱스 값을 -1로 변경. -1은 고장난 신호등을 표시
for i in range(b):
    lst[int(input())-1] = -1

# 연속된 k개의 신호등에서 고장난 신호등의 개수 카운트
Min = cnt = lst[:k].count(-1)

# Slide window algo 사용해서 최소값 계산 후 출력
for i in range(1, n -(k-1)):
    if lst[i-1] == -1 :
        cnt -= 1
    if lst[i+k-1] == -1:
        cnt+= 1
    Min = min(cnt, Min)
print(Min)