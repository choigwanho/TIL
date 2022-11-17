# 8958 OX퀴즈
def sol8958():
    add=1
    cnt_list=[]

    for i in range(int(input())):
        cnt_list.append(0)
        tmp = list(str(input()))

        for j in range(len(tmp)):
            if tmp[j]=='O':
                cnt_list[i]=cnt_list[i]+add
                if tmp[j]==tmp[j+1]:
                    add+=1
                else:
                    add=1

    for cnt in cnt_list:
        print(cnt)