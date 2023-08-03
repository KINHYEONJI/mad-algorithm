input_number = list(map(int, input()))
# bucket 생성
bucket = [0]*10

#각 숫자가 몇 개 있는지 파악
for i in input_number:
    bucket[i] += 1
#bucket 값 복사
newlist = bucket[:]

max_bucket = max(bucket)
result = 0
# 6+9 최댓값
bucket69 = (bucket[6] + bucket[9])//2 +(bucket[6] + bucket[9])%2

for j in range(10):
    if bucket[6] == max_bucket: #6이 가장 많을 때
        newlist[6] = 0
        new_max = max(newlist)
        if bucket69 >= new_max: #6, 9갯수의 합이 최댓값보다 크면
            result = bucket69
        else:
            result = new_max
        
    elif bucket[9] == max_bucket: #9가 가장 많을 때
        newlist[9] = 0
        new_max = max(newlist)
        if bucket69 >= new_max: 
            result = bucket69
        else:
            result = new_max
            
    else:
        if bucket[j] == max_bucket:
            result = max_bucket

print(result,end='')