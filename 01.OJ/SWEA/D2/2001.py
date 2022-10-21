# 파리 퇴치
def findSum(arr,x,y):
    rst = 0
    for i in range(x,x+M):
        rst += sum(arr[i][y:y+M])
    return rst
        

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            ans = max(ans, findSum(arr,i,j))
    print(f'#{t} {ans}')