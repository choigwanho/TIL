# 1018 체스판 다시 칠하기
"""
[입력] 
n개의 문자열을 입력받는다.
[알고리즘] 
1. 8*8로 구할 수 있는 모든 경우, n-7, m-7 인덱스로 모두 탐색
2. 첫번째가 'B' or 'W' 인 경우를 고려해 모든 경우 cnt해서 최소값을 저장
[출력]
그 중 최소값을 출력
"""
def sol1018():
    n,m=map(int,input().split())
    board=list()
    cnt=list()

    for _ in range(n):
        board.append(input())

    for i in range(n-7):
        for j in range(m-7):
            blackCase=0
            whiteCase=0
            for a in range(i,i+8):
                for b in range(j,j+8):
                    if (a+b)%2==0:
                        if board[a][b]!='B': 
                            blackCase+=1
                        if board[a][b]!='W': 
                            whiteCase+=1
                    else:
                        if board[a][b]!='W': 
                            blackCase+=1
                        if board[a][b]!='B': 
                            whiteCase+=1
            cnt.append(min(blackCase,whiteCase))
    print(min(cnt))