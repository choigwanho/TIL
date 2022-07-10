# 2439 별 찍기 - 2
def sol2439():
    n = int(input())
    for i in range(1,n+1):
        print(("*"*i).rjust(n))