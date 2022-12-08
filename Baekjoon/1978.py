import sys
si = sys.stdin.readline

# 1000 이하의 자연수
def sol(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

# 100이하의 수
n = int(si())
nums = list(map(int,si().split()))
cnt = 0
for num in nums:
    if sol(num):
        cnt+=1

print(cnt)