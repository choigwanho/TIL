import sys, heapq
si = sys.stdin.readline

n = int(si()) # 강의 개수 n
time = list()
for _ in range(n):
    s, e = map(int,si().split()) # 강의 시작 시간, 종료 시간
    heapq.heappush(time, (e,s)) # 끝나는 시간 오름차순으로, 그 다음으로 시작시간이 작은 순

end = 0 # 종료시간 초기화
cnt = 0 # 구하려는 값

while time:
    if time[0][1] >= end: # 시작시간과 이전 수업 종료시간 비교, 겹쳐도 됨 (==)
        end = heapq.heappop(time)[0] # 종료시간 갱신, 끝나는 시간이 가장 빠른 것으로 갱신됨으로 그리디하게 원하는 결과를 얻을 수 있음
        cnt += 1 
        continue
    heapq.heappop(time) # 해당하지 않는 경우 heappop
print(cnt)