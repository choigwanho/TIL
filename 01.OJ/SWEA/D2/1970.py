# 쉬운 거스름돈
T = int(input())
for t in range(1,T+1):
    N = int(input())

    cash_list = [50000,10000,5000,1000,500,100,50,10]
    
    ans = list()
    
    for cash in cash_list:
        ans.append(N//cash) 
        N=N%cash

    print(f'#{t}')
    print(*ans)