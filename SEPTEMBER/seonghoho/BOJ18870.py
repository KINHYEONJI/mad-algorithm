N = int(input())
lst = list(map(int, input().split()))

copy_lst = lst[:] # 내용만 복사한 배열 생성

copy_lst.sort() # 배열 오름차순으로 정렬

set_lst = list(set(copy_lst))  # set으로 중복 제거 후 리스트로 만들기

ndx_num = {}    # 딕셔너리 생성
for i in range(len(set_lst)):   # 중복제거, 오름차순 정렬된 배열 값을 key, 인덱스를 value로 할당
    ndx_num[set_lst[i]] = i

for i in range(N):  # lst에 주어진 숫자를 key로 넣어 value값 출력
    print(ndx_num[lst[i]], end=' ')