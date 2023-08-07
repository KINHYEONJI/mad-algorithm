"""
텍스트랑 단어 입력받고 텍스트를 단어 단위로 쪼개서 리스트를 만든다.
리스트 인덱스 수 -1이 단어 단위로 쪼갠 수가 되고 이는 인덱스 중복없이 텍스트에 등장한 단어 수가 된다.
"""
text= input()
word= input()
arr = text.split(word)
print(len(arr)-1)
