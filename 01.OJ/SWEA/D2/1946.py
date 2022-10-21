# 간단한 압축 풀기
T = int(input())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]   
for t in range(1,T+1):
    N = int(input())
    S = ''
    for _ in range(N):
        c,k = map(str,input().split())
        S += c*int(k)
    print(f'#{t}')
    lst = 0
    for i in range(len(S)//10):
        lst = 10*(i+1)
        print(S[10*i:10*(i+1)])
    print(S[lst:])