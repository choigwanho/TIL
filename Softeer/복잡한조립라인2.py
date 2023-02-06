'''
k개의 조립라인에 n개의 작업장이 있을 때, 작업을 가장 빨리 끝내는 시간을 구하는 문제
조립라인을 병렬로 두고 각 작업장에서 최소 작업시간이 걸리는 루트를 선정한다. 그리고 그 경로에서 이동이 있는지 없는지로 구분하여
for문으로 누적해주면 O(KN) 으로 해결이 가능하다.
최소값을 구하기 위해 경로 이동이나 복잡한 변수가 있는 경우 조건문으로 분기처리하여 min 또는 max를 활용해서 값을 갱신해주면 다른 문제에서도
시간효율적으로 풀 수 있을 것같다.
어떤 기준으로 값을 추출해서 갱신해줄지 설정하는 컨셉이 중요한 것 같다.
문제를 보고 잘 활용해보자.
'''
import sys
si = sys.stdin.readline

k, n = map(int, si().split()) # 조립라인의 수 k, 작업장의 수 n

work = [] # 같은 레벨의 작업장 작업시간 저장
switch = [] # 다음 레벨로 이동하는 시간 저장

for _ in range(n-1): # O(n) = 100
    info = list(map(int, si().split()))
    work.append(info[:k]) # 작업시간
    switch.append(info[-1]) # 이동시간
work.append(list(map(int, si().split()))) # 마지막 라인은 이동 시간이 없으므로 따로 추가

for i in range(n-1): # O(n*k) = 100만
    min_work = min(work[i]) # i번째 레벨 작업장에서 가장 짧은 작업시간
    for j in range(k):
        if min_work==work[i][j]: # 최소값이 같은 라인인 경우 이동시간 없이 누적
            work[i+1][j] += work[i][j]
        else: # 최소값이 아닌 경우 최소값과 이동시간을 합친 값이 같은 라인의 마지막 작업시간보다 작은지 비교해서 누적
            work[i+1][j] += min(work[i][j], min_work + switch[i])

print(min(work[-1]))

