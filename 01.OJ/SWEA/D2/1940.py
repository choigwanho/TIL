# 가랏! RC카!
T = int(input())
for t in range(1,T+1):
    N = int(input())
    ans = 0
    v=0
    for _ in range(N):
        info = list(map(int,input().split()))
        command = info[0]
        if command==1:
            v += info[1]
        elif command==2:
            v -= info[1]
        if v < 0:
            v =0
        ans += v

    print(f'#{t}',ans)
