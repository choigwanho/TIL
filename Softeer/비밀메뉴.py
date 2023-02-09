import sys 
si = sys.stdin.readline

m,n,k = map(int,si().split()) # 비밀 메뉴 버튼 조작 개수 m, 사용자 버튼 조작 개수 n, 버튼의 개수 k
ml = list(map(int,si().split())) # 비밀 메뉴 조작법
nl = list(map(int,si().split())) # 사용자의 버튼 조작


# 사용자가 비밀 메뉴 식권을 받을 수 있다면 secret, 그렇지 않다면 normal 출력
if n < m:
    print("normal")
else:
    if str(ml)[1:-1] in str(nl): # O(n) = 100
        print("secret")
    else:
        print("normal")