N=int(input()) #____가 4로 나누면 몇 레벨에서 답변이 나오는지 알 수 있다
def abc(level):

    if level==N: #_*8개 구분이 한 줄일걸로 if에 해당하는 부분 안에 넣어 구현
        print(('_' * (4 * level)) + "\"재귀함수가 뭔가요?\"")
        print(('_' * (4 * level)) + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(('_' * (4 * level)) + '라고 답변하였지.')
        return

    print(('_'*(4*level))+"\"재귀함수가 뭔가요?\"")
    print(('_'*(4*level))+'\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(('_'*(4*level))+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(('_'*(4*level))+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"')
    abc(level+1) #if 만족 후 돌아오는 부분에 프린트할 내용
    print(('_' * (4 * level)) + '라고 답변하였지.')


print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
abc(0)