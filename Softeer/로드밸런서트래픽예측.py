from collections import deque
import sys
si = sys.stdin.readline

n,k = map(int,si().split()) # 서버의 개수 n, 요청의 개수 k
 
graph = list({} for _ in range(n+1)) # 10만
cnt = [0]*(n)

for i in range(1,n+1): # O(n) = 10만
    server = list(map(int,si().split()))
    if server[0] > 0: # r > 0 이면 i번째 서버는 로드 밸랜서
        graph[i]["x"] = 1 
        graph[i]["server"] = server 
    elif server[0] == 0:
        graph[i]["server"] = server
            
for i in range(k): # k번의 요청, 1e18 -> 시간복잡도가 큼

    q = deque([1]) # 요청은 루트 노드에서 시작
    while q: # 60만
        cur = q.popleft()
        cnt[cur-1] += 1 # cnt 증가
        if graph[cur]["server"][0] > 0: # 로드밸랜서
            q.append(graph[cur]["server"][graph[cur]["x"]])
            graph[cur]["x"] = (graph[cur]["x"] % graph[cur]["server"][0]) + 1 # x값 갱신, 라운드 로빈

print(*cnt)