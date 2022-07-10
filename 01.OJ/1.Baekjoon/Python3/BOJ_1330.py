# 1330 두 수 비교하기 
def sol1330():
    a,b=map(int,input().split())
    if a<b:
        print("<")
    if a>b:
        print(">")
    if a==b:
        print("==")