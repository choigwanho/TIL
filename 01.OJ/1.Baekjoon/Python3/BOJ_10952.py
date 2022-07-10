# 10952 A+B - 5
def sol10952():
    a=1
    b=1
    sums=[]
    while a+b!=0:
            a, b = map(int, input().split())
            if a+b!=0:
                sums.append(a+b)

    for sum in sums:
        print(sum)