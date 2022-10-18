# 연월일 달력
T = int(input())
for t in range(1, T+1):
    ymd = str(input())
    yyyy, mm, dd = int(ymd[:4]), int(ymd[4:6]), int(ymd[6:])

    if not (1<=mm<=12):
        print(f'#{t} {-1}')
        continue
    else:
        if mm in [1,3,5,7,8,10,12]:
            if not (1<=dd<=31):
                print(f'#{t} {-1}')
                continue
        elif mm in [4,6,9,11]:
            if not (1<=dd<=30):
                print(f'#{t} {-1}')
                continue
        elif mm == 2:
            if not (1<=dd<=28):
                print(f'#{t} {-1}')
                continue
        print(f'#{t} {ymd[:4]}/{ymd[4:6]}/{ymd[6:]}')