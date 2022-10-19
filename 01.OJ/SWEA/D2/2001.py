# 파리 퇴치
T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N-M):
        for j in range(N-M):
            ans+=sum(arr[i][j:j+M])
            
    print(f'#{t} {ans}')