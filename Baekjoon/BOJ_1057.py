# 1057 단어 공부
def sol1057():
    char_list = list(str(input()).upper())
    char_set = list(set(char_list))

    cnt_char = [0]*len(char_set)

    max_list = []

    for i, set_char in enumerate(char_set):
        for list_char in char_list:
            if set_char==list_char:
                cnt_char[i]+=1

    for i, cnt in enumerate(cnt_char):
        if max(cnt_char)==cnt:
            max_list.append(char_set[i])

    if len(max_list)==1:
        print(max_list[0])
    else:
        print("?")