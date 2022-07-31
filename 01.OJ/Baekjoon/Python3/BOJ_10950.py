# 10950 A+B - 3
def sol10950():
    sums=[]

    for _ in range(int(input())):
        a,b=map(int,input().split())
        sums.append(a+b)

    for sum in sums:
        print(sum)