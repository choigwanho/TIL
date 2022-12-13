import sys
si = sys.stdin.readline

# 두 정수 n,m. 각각 10만, 20억
n,m = map(int,si().split())
# n개의 정수로 이루어진 수열 A[]. 수열의 수는 중복가능. 각 수는 최대 10억 ~ 최소 -10억
a = list()
for _ in range(n):
    a.append(int(si()))

a.sort()

ans = sys.maxsize
l,r = 0,1
while l<n and r<n:
    diff = abs(a[r]-a[l])
    # 차이가 m 보다 작은 경우 오른쪽 이동
    if diff < m: 
        r+=1
        continue
    # 차이가 m 이상일 때 차이의 최소값 갱신후 왼쪽 이동
    ans = min(ans,diff)
    l+=1
print(ans)