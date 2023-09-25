"""
한 세트에 0 ~ 9 1개씩
6 과 9는 동등취급
방번호 주어졌을 때 필요한 세트
"""
# 방 번호를 요소 하나씩 쪼개서 리스트화
nums_lst = list(map(int, input()))

# DAT --> bucket생성 --> 값넣고 맥스 출력
bucket = [0] * 10
"""
입력받은 숫자들의 길이만큼 loop
만약 nums_lst의 i번 인덱스의 값이 6 이거나 9가 나왔을 때
bucket 6번 인덱스와 9번 인덱스를 동등하게 +1씩 카운트
가장 많이 카운트 된 bucket 인덱스의 값이
문제에서 요구하는 세트의 개수 최솟값 
"""
for i in range(len(nums_lst)):
    if nums_lst[i] == 6 or nums_lst[i] == 9:
        if bucket[6] <= bucket[9]:
            bucket[6] += 1
        else:
            bucket[9] += 1
    else:
        bucket[nums_lst[i]] += 1

print(max(bucket))
