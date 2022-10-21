# 초심자의 회문 검사
T = int(input())
for t in range(T):
    S = str(input())
    l = len(S)
    mid = l//2

    ans = 0
    if l%2==0 and S[:mid][::-1] == S[mid:]: # 짝수
        ans =1
    elif l%2!=0 and S[:mid][::-1] == S[mid+1:]: #홀수
        ans = 1     
        
    print(f'#{t+1} {ans}')