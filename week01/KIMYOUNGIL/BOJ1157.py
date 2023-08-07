st = input().upper()

bucket = [0]*26
for i in range(len(st)):
    bucket[ord(st[i])-ord('A')] += 1

bucket_set = sorted(bucket)
if bucket_set[-1] == bucket_set[-2]:
    print("?")
else:
    print(chr(bucket.index(max(bucket))+ord('A')))