'''
input
5
2 3 1 2 2
ouput
2
'''
import sys
si = sys.stdin.readline

n = int(si()) # 모험가의 수
fear = list(map(int,si().split())) # 각 모험가의 공포도 값

fear.sort() # 오름차순 정렬 -> 그룹의 수가 최대가 되기 위해서 작은 공포도로 시작하여 x명 이상이 되도록 그룹화

group = 0
member = 0
for x in fear:
    member += 1
    if member >= x: # 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 그룹에 참여해야 함 
        group += 1
        member = 0

print(group) # 여행을 떠날 수 있는 그룹의 수의 최댓값 출력