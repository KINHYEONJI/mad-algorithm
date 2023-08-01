h,m = map(int,input().split())
num = int(input())

new_m = (m+num) % 60
new_h = h+(m+num)//60
if new_h > 23:
    new_h = new_h-24

print(new_h,new_m)