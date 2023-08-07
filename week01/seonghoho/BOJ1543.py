lst = list(input())     # 문서
tg = list(input())      # 타겟
ndx = 0                 # 문서의 인덱스 값
sum_ = 0                # 타겟 개수

while ndx < len(lst):                   #인덱스가 문서 길이보다 작을 때 실행
    mid = 0
    for i in range(len(tg)):            # 타겟의 글자와 문서 비교 
        if (i + ndx) < len(lst):        #인덱스 범위 벗어날 경우를 위한 안전장치
            if lst[i + ndx] == tg[i]:   # 타겟의 문자와 문서의 문자가 같다면 mid+=1
                mid += 1
    if mid == len(tg):                  # 타겟의 길이와 일치값 mid가 같다면
        ndx += len(tg)                  # 인덱스를 타겟만큼 증가
        sum_ += 1                       # 타겟 개수 1 증가
    else:
        ndx += 1                        # 타겟의 길이와 일치값이 다르면 인덱스 값 1 증가
print(sum_)
 