import sys
si = sys.stdin.readline 

n = int(si()) # 단계 n

# Diamond-Square-Algorithm
# 정사각형을 이루는 점 4개를 고르고 각 변의 중앙에 점을 하나 추가하고 중심에 점을 하나 추가
dp = [0]*(n+1)
dp[0] = 2

for i in range(1,n+1):
    dp[i] = dp[i-1] + (dp[i-1]-1) # i 번째의 한 변의 점의 개수는 (i-1 번째 점의 개수 + (i-1 번째 점의 개수 - 1)) 이다.  

print(dp[n]**2) # 점의 개수가 한변의 제곱개수로 들어난다.
