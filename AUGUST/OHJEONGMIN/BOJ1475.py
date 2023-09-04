room_num = list(map(int, input()))
bucket = [0] * 10

for i in range(len(room_num)):
    if room_num[i] == 6 or room_num[i] == 9:
        if bucket[6] == bucket[9]:
            bucket[6]+=1
        else:
            bucket[9]+=1
    else:
        bucket[room_num[i]]+=1

print(max(bucket))

