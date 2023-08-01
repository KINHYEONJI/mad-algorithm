num_1, num_2 = map(int,input().split())

result_1=1
for i in range(2,(max(num_1,num_2)+1)):
    if num_1 % i ==0 and num_2 % i ==0:
        result_1=i

a = num_1//result_1
b = num_2//result_1

result_2= result_1 * a * b

print(result_1)
print(result_2)

#11