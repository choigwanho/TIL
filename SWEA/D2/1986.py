# 지그재그 숫자
T = int(input())
for t in range(1,T+1):
    N = int(input())
    ans = 0
    for n in range(1, N+1):
        if n%2==0:
            ans -= n
        else:
            ans += n
    print(f'#{t} {ans}')