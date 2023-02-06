'''
신차의 크기를 결정하는 문제
n명의 소비자에게 신차의 구매의사를 조사한다.
소비자는 a개의 "신차의 크기가 s이상이라면 차량 한대를 p원에 구매할 용의가 있다"라는 정보를 준다.

m개의 매출 시나리오를 만족하기 위한 신차의 크기가 최소 얼마여야 하는지 구해야 한다.


소비자는 여러가지 계획을 가지고 있고, 테스트 시나리오에 따라서 소비자의 계획을 모두 찾아봐야한다.

투플형태로 우선순위 큐를 넣을지, 정렬을 할지 고민이다.

순회할 것이기 때문에 배열로 모든 정보를 저장하는 건 OK 

'''
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
    



# 시나리오 이상의 매출을 낼 수 있다면 신차의 최소 크기, 없다면 -1 출력
print(*answer)
 