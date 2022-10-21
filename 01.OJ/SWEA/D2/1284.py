# 수도 요금 경쟁
def costA(w,p):
    return w*p

def costB(w,q,r,s):
    if w <= r:
        return q
    else:
        return q + s*(w-r)

T = int(input())
for t in range(1,T+1):
    P, Q, R, S, W = map(int, input().split())   
    print(f'#{t} {min(costA(W,P),costB(W,Q,R,S))}')