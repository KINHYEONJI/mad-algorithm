#find_st에 해당하는 문자열을 1로 바꿔서 1을 카운트 해주기
#문자열.replace(바꾸려는 문자열,바꾸려는 값)
st = input()
find_st =input()
new_st = st.replace(find_st,'1')
lst = list(new_st)
print(lst.count('1'))

