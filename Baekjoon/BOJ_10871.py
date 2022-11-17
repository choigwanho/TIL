# 10871 X보다 작은 수
def sol10871():
    n,x=map(int,input().split())
    nums=list(map(int,input().split()))

    for num in nums:
        if num<x:
            print(num,end=" ")