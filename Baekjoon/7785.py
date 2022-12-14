import sys
from collections import defaultdict
si = sys.stdin.readline

# 로그에 기록된 출입 기록의 수 n input, 2 <= n <= 10**6
n = int(si())

# defaultdict 선언
log = defaultdict(list)

for _ in range(n):
    # n개의 줄에 출입 기록 input, 사람의 이름,"enter"/"leave"
    name, status = map(str,si().split())
    # 이름을 key로 갖고 출입 상태 list를 value로 갖도록 초기화, 회사에는 동명이인이 없음으로 이름을 dict의 key로 사용가능
    log[name].append(status)

# 현재 회사에 있는 모든 사람을 구하기
ans_list = []
for name, status_list in log.items():
    if len(status_list)%2!=0:
        ans_list.append(name)

# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력
ans_list.sort(reverse=True)
print(*ans_list,sep="\n")