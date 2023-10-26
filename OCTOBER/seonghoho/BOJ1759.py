'''
서로 다른 L개의 알파벳 소문자로 구성
한 개 이상의 모음 a e i o u
두 개 이상의 자음으로 구성

암호에서 증가하는 순서로 배열되었을 것
점점 증가하는 알파벳

c개의 문자를 조합하여 암호 구해라
'''
l, c = map(int, input().split())

lst = list(input().split())
lst.sort()
mother = ['a', 'e', 'i', 'o', 'u']
numbers = [''] * l


# 조합 돌리고, 모 1, 자 2 이상인지 리스트 돌려서 확인하고 맞으면 출력
def dfs(level, start):
    if level == l:
        mo = 0
        ja = 0
        for i in numbers:
            if i in mother:
                mo += 1
            else:
                ja += 1
        if mo >= 1 and ja >= 2:
            res = ''.join(numbers)
            print(res)
        return # 리턴 들여쓰기 주의할 것
    for i in range(start, c):
        numbers[level] = lst[i]
        dfs(level + 1, i + 1)


dfs(0, 0)
