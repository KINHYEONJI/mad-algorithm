# 접근:
# 1. 최빈값의 빈도수(최빈치)
# 2. 6과 9는 대체 가능 -> 6과 9는 한 세트로 처리

lst = list(map(int, input()))       # 입력 받은 수를 리스트로 정렬

max_cnt = 0
for i in range(10):
    if i == 6 or i == 9:        # 6과 9는 한 세트로 처리
        cnt = (lst.count(6) + lst.count(9) + 1) // 2     # 6과 9의 개수를 합친 뒤에도, 한 세트에 최소한 하나씩은 들어가야 함.
                                                        # -> 6과 9의 개수 합에 1을 더한 뒤, 2로 나누는 것임.
    else:
        cnt = lst.count(i)

    if cnt > max_cnt:           # 최빈치 구하기
        max_cnt = cnt

print(max_cnt)