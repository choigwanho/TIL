# 2908 상수
def sol2908():
    a,b=map(str,input().split())

    if int(a[::-1])>int(b[::-1]):
        print(int(a[::-1]))
    if int(a[::-1])<int(b[::-1]):
        print(int(b[::-1]))