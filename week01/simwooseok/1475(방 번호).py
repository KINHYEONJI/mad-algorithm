num = list(map(int, input()))
bucket = [0] * 10

for i in range(len(num)):
    if num[i] == 6 or num[i] == 9:
        if bucket[6] == bucket[9]:
            bucket[6] += 1
        
        else: bucket[9] += 1

    else:
        bucket[num[i]] += 1

print(max(bucket))