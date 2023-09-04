

word = input()
small = input()
result = word.split(small)

print(len(result)-1)


# 밑은 그냥 구해보려다 실패한 코드
# str_r=list(input())
# str_y=list(input())

# a=len(str_r)
# b=len(str_y)

# def strc(x):
#     c=0
#     for i in range(b):
#         if str_r[x+c] == str_y[c]:
#             c+1
#             continue
#         else:
#             return 0
#     return 1

# for i in range(b):
#     max=-21e8
#     count=0
#     skip=0
#     for j in range(0+i,a-(b-1)):
#         if skip>0:
#             skip -=1  
#             continue  
#         count+=strc(j)
#         if strc(j) ==1:
#             skip=b-1

#     if count>max:
#         max=count

# print(count)  