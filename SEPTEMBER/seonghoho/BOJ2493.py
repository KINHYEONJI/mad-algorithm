N = int(input())
llst = list(map(int, input().split()))
lst = [0]
lst.extend(llst)  # 입력 받은 리스트 앞에 0 추가
mid = []
res = []

for i in range(1, N + 1): # 인덱스 1부터 대입 하기 위한 range 범위 설정
    mid.append([i, lst[i - 1]]) # mid에 인덱스와 이전 값 묶어서 추가
    if mid:
        while mid:
            if mid[-1][1] > lst[i]: # mid에 마지막으로 추가한 리스트의 1번 인덱스,
                                    # 즉, lst[i] 값의 바로 전 값과 비교하는 부분
                res.append(mid[-1][0] - 1) # 인덱스 값에서 -1한 값 추가
                break
            else: # 이전 값이 더 크지 않다면 그 배열 pop해서 제거하고 다음 수 비교
                mid.pop()
    if len(res) != i: # res의 길이와 i가 다르면 이번 while문에서 추가안했다는 뜻이므로
        res.append(0) # 해당 값보다 큰 값이 없다는 뜻이니 0추가

print(*res) # 추가한 값만 출력