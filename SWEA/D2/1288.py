# 새로운 불면증 치료법
T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = set()
    cnt=0
    while len(nums) != 10:
        cnt+=1
        nums.update(set(str(N*cnt)))
    print(f'#{t} {N*cnt}')
 