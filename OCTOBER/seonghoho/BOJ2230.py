N, M = map(int, input().split())
lst = []
for i in range(N):  # 주어진 수 lst에 입력
    a = int(input())
    lst.append(a)

llst = list(set(lst))   # set 이용해서 중복 수 제거, 불필요한 비교 줄이기 위함
llst.sort() # sort를 이용하여 정렬 후 투 포인터로 접근
low, high = 0, 0
Min = 21e8
cnt = 0
minus = 0

while 1:
    if minus >= M:  # 두 값의 차이가 크거나 같을 때
        if Min > minus: # minus의 최솟값 저장
            Min = minus
        low += 1    # low  하나 높여서 minus 값 줄이기
    else:
        if high == len(llst)-1: # high 값이 sort한 llst의 길이-1이면,
            break               # 이미 두 값의 차이가 M보다 작은데 점점 작아질 일만 남으니 break
        high += 1   # 두 값의 차이가 M보다 작으면 high +1

    minus = llst[high] - llst[low]  # minus 값 갱신
    if low == len(llst)-1:  # low가 마지막까지 가면 break
        break
print(Min) # Min값 출력