import sys
si = sys.stdin.readline

n = int(si()) # 작업장의 수 n
work = list() # 작업시간
switch = list() # 작업장 이동시간

for _ in range(n-1):
    info = list(map(int,si().split())) # 작업시간과 작업장 이동시간 info
    work.append(info[:2])
    switch.append(info[2:])
work.append(list(map(int,si().split()))) # 마지막 info는 작업시간만 주어지므로 따로 append

for i in range(n-1):
    work[i+1][0] += min(work[i][0],work[i][1]+switch[i][1]) # a라인에서 그대로 작업하는 경우와 b작업장에서 이동하는 경우 중 작은 값 누적 
    work[i+1][1] += min(work[i][1],work[i][0]+switch[i][0]) # b라인에서 그대로 작업하는 경우와 a작업장에서 이동하는 경우 중 작은 값 누적

print(min(work[-1]))