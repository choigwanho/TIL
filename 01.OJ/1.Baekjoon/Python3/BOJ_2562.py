# 2562 최대값
def sol2562():
    nums=[]

    for _ in range(9):
        nums.append(int(input()))

    print(max(nums))
    print(nums.index(max(nums))+1)