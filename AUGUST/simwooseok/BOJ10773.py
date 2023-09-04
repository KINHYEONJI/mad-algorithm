K = int(input())        
arr = []
for i in range(K):
    num = int(input())      # k번 정수를 받지만 0일때는 pop() 아닐때 append()
    if num == 0:    
        arr.pop()
    else:
        arr.append(num)
print(sum(arr))
    
