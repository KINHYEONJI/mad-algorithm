def ca(a):
    if a==0:
        return 0
    
    if a<10:
        a * 10

    num_1 = a // 10
    num_2 = a % 10
    num_3 = (num_1 + num_2) % 10

    result = (num_2 * 10) + num_3


    return result

n=int(input())
m=n
count = 0
for i in range(100):
    num=ca(m)
    count +=1
    m=num
    if num == n:
        print(count)
        break
    

