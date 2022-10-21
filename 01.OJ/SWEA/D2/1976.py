# 시각 덧셈
T = int(input())
for t in range(1,T+1):
    hh1, ss1, hh2, ss2 = map(int, input().split())
    
    hh = hh1+hh2
    mm = ss1+ss2
    if mm > 60:
        hh += mm//60
        mm = mm-60
    elif mm == 60:
        hh += mm//60
        mm = 1
        
    if hh > 12:
        hh -= 12 

    print(f'#{t} {hh} {mm}')