# 두 개의 숫자열
def cal(arr1, arr2):
    total = 0
    for a,b, in zip(arr1, arr2):
        total +=a*b
    return total
    
T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))

    ans  = 0
    
    if N==M:
        ans = cal(a_list, b_list)
    elif N>M:
        for i in range(N-M+1):
            ans = max(ans, cal(a_list[i:],b_list))
    elif N<M:
        for i in range(M-N+1):
            ans = max(ans, cal(a_list,b_list[i:]))

    print(f'#{t} {ans}')

