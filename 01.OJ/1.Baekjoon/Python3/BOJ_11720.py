# 11720 숫자의 합
def sol11720():
    n=int(input())
    num=list(str(input()))
    sum=0

    for i in num:
        sum+=int(i)

    print(sum)