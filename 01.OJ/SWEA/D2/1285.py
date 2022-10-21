# 아름이의 돌 던지기
T = int(input())
for t in range(1,T+1):
    N = int(input())
    dis = [abs(n) for n in list(map(int,input().split()))]
    m = min(dis)
    cnt = dis.count(m)

    print(f'#{t} {m} {cnt}')