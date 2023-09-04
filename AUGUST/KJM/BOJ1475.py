nums = list(map(int,input()))
bucket = [0] * 10

for i in range(len(nums)):
    
    if nums[i] == 6 or nums[i] == 9:
        if bucket[6] == bucket[9]:  # 버켓에서 6의 개수와 9의 개수가 같으면
            bucket[6] += 1   # 버켓에서 6의 개수에 1 증가
        else:
            bucket[9] += 1  # 다르면 버켓에서 9의 개수에 1 증가
    else:      
        bucket[nums[i]] += 1    # nums의 값은 bucket의 인덱스 , 찾을 때마다 해당 인덱스 +=1
    
print(max(bucket))
