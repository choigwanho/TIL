import sys
si = sys.stdin.readline

n = int(si()) # 계단의 개수
floor = [0] + list(int(si()) for _ in range(n)) # 계단에 쓰여있는 점수

dp = [0]*(n+1)

dp[1] = floor[1]
for i in range(2,n+1):
    dp[2] = floor[1] + floor[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-2], dp[i-3] + floor[i-1]) + floor[i]

print(dp[n])