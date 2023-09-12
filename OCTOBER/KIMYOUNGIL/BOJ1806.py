n,s = map(int,input().split())
arr = list(map(int,input().split()))

def two_pointer():
    ans,start,end,length = arr[0],0,0,21e8
    while 1:
        if ans < s:
            end += 1
            if end < n: ans += arr[end]
            else:
                start += 1
                end = n-1
        else:
            length = min(length,end-start+1)
            ans -= arr[start]
            start += 1

        if start == n:
            if length == 21e8: return print(0)
            else: return print(length)
two_pointer()