# 간단한 소인수분해
T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = []
    
    for num in [2,3,5,7,11]:
        cnt = 0 
        while True:
            if N%num==0: 
                N = N//num
                cnt += 1
            else:
                nums.append(cnt)
                break
    print(f'#{t}',*nums)
