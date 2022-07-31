# 1065 직사각형에서 탈출
"""
[입력]
4개 숫자 입력
[알고리즘]
경계선까지의 거리 계산
[출력]
거리중 최소값 출력
"""
def sol1065():
    x,y,w,h=map(int,input().split())
    l=[ x, w-x, y, h-y ]
    print(min(l))