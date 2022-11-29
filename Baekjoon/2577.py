# 2577 숫자의 개수
def sol2577():
    a = int(input())
    b = int(input())
    c = int(input())

    num_char=list(str(a*b*c))
    num_cnt=0
    for i in range(10):
        for j in num_char:
            if i==int(j):
                num_cnt+=1
        print(num_cnt)
        num_cnt=0