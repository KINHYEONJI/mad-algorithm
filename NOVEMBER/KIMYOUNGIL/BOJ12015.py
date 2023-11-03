n = int(input())
arr = list(map(int,input().split()))

def binarysearch(s,e,target):
    while 1:
        mid = (s+e)//2
        if result[mid] < target <= result[e]:
            s = mid
        elif result[s] < target <= result[mid]:
            e = mid
        if abs(s-e) == 1:
            return e

result = [arr[0]]
for i in range(1,n):
    if result[-1] < arr[i]:
        result.append(arr[i])
    else:
        if result[0] >= arr[i]:
            result[0] = arr[i]
        else:
            idx = binarysearch(0,len(result)-1,arr[i])
            result[idx] = arr[i]

print(len(result))
