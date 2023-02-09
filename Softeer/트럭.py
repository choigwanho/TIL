from collections import defaultdict
from bisect import bisect_right, bisect_left
import sys
si = sys.stdin.readline

n = int(si()) # 소비자 조사 횟수
consumer = list() # 소비자 제안 정보

for _ in range(n): # 10만
    tmp = list(map(int, si().split())) 
    a = tmp[0]
    proposal = list()
    for i in range(1, a+1): # 50만
        s, p = tmp[2*i-1], tmp[2*i]
        proposal.append((s,p))
    proposal.sort()
    consumer.append(proposal)

m = int(si()) # 시나리오의 개수
scenario = list(map(int, si().split())) # 시나리오 정보

answer = list() # 매출을 낼 수 있는 신차의 정보 저장 

for q in scenario: # 10만
    q



# 시나리오 이상의 매출을 낼 수 있다면 신차의 최소 크기, 없다면 -1 출력
print(*answer)