# 중간 평균값 구하기
T = int(input())
for t in range(1,T+1):
    nums = list(map(int, input().split()))
    ans = round((sum(nums)-max(nums)-min(nums))/8)
    print(f'#{t} {ans}')