'''
투포인터로 오른쪽을 이동시켜가면서 탐색
'''
import sys
si = sys.stdin.readline

n = int(si()) # 돌의 개수
h = list(map(int, si().split())) # 돌의 높이
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if h[i] > h[j]: 
            dp[i] = max(dp[i], dp[j]+1)

# 높이가 점점 높은 돌을 밟으면서 개울을 지나려고 할 때, 밟을 수 있는 돌의 최대 개수 출력
print(max(dp))
