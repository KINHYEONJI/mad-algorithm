N=int(input()) #N받아줍니다

def factorial(a): #팩토리얼 함수 선언
    result=1
    if a>0:
        result = a * factorial(a-1) #  쭈욱가면 .....*1이 나온다 n!  완성..!

    return result
    

print(factorial(N))