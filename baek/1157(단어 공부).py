words = input().upper()
words_eq = list(set(words)) #set함수로 중복값 제거

cnt_list = []

for i in words_eq:
    cnt = words.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1: 
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(words_eq[max_index])
