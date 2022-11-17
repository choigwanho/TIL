# 날짜 계산기
T = int(input())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]   
for t in range(1,T+1):
    mm1, dd1, mm2, dd2 = map(int,input().split())
    ans = -dd1+dd2+1
    for mm in range(mm1,mm2):
        ans+=days[mm]
    print(f'#{t} {ans}')
