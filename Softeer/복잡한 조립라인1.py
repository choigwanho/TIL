import sys
from collections import defaultdict
si = sys.stdin.readline

k, n = map(int, si().split()) # 라인의 수 k, 작업장의 수 n

work = list() # 작업시간
switch = list() # 작업장 이동시간

for _ in range(n-1):
    info = list(map(int,si().split())) # 작업시간과 작업장 이동시간 info
    work.append(info[:k])

    switch_dict = defaultdict(int)
    idx = 0
    for i in range(k):
        for j in range(k):
            if i==j:
                continue
            switch_dict[(i,j)] = info[k+idx]
            idx+=1
    switch.append(switch_dict)
    
work.append(list(map(int,si().split()))) # 마지막 info는 작업시간만 주어지므로 따로 append

for i in range(n-1):
    for j in range(k):
        m = work[i][j]
        for c in range(k):
            if j==c:
                continue
            m = min(m, work[i][c] + switch[i][(c, j)])
        work[i+1][j] += m

print(min(work[-1]))