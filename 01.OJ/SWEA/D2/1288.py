# 새로운 불면증 치료법
T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = set([])
    for num in range(N,1000001,N):
        nums= set.union(nums,set(list(str(num))))
        print(nums, len(nums))
        if len(nums) == 10:
            print(f'#{t} {num}')
            break  