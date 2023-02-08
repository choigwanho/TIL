import sys 
si = sys.stdin.readline

a,b = map(int,si().split())

if a==b:
    print("same")
elif a>b:
    print("A")
elif a<b:
    print("B")
