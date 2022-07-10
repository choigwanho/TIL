# 2920 음계
def sol2920():
    nums=list(map(int,input().split()))
    cnt=0

    for i in range(7):
        if nums[i]<nums[i+1]:
            cnt+=1

    if cnt==7:
        print("ascending")
    elif cnt==0:
        print("descending")
    else:
        print("mixed")