'''
스택문제
0을 입력 받으면 pop
나머지는 append
'''

stack = []

T = int(input())

for _ in range(T): # 루프 넘버
    
    input_num = int(input()) # 1.겟 넘

    if input_num == 0: # 2. 겟 0, 팝 라스트인
        stack.pop() 
        
    else:
        stack.append(input_num) # 3. 겟 엘스, 어팬드 인풋넘
        

print(sum(stack)) # 4. 프린트 썸 오브 스택 아웃 
        
    