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

# 1181 단어 정렬
"""
[입력]
입력받은 숫자만큼 반복하여 문자 입력
[알고리즘]
1. set()으로 중복제거하여 list() 저장
2. 사전순정렬 길이순으로 정렬
[출력]
반복문으로 출력
"""
def sol1181():
    n = int(input())
    words = set(input() for _ in range(n))
    wordList=list(words)

    wordList.sort()
    wordList.sort(key=len)

    for word in wordList:
        print(word)



# 1259 팰린드롬수
def sol1259():
    n=1
    nums=[]
    while n!=0:
        n = int(input())
        if n==0:
            break
            nums.append()
    
    for num in nums:
        if num%2==0:
            for i in range(len(num)):
                if num[i]==num[-1-i]:

        else:

    


        


