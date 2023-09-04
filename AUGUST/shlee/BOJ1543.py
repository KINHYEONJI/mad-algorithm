st = input()
target = input()

count_st = st.count(target)
print(count_st)

new_st = st.split(target)
print(len(new_st)-1)
