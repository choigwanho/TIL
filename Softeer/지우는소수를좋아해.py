from heapq import heappush, heappop
from math import sqrt
import sys
si = sys.stdin.readline

n, m = map(int,si().split()) # 체육관의 개수 n, 체육관 사이 길의 개수 m
graph = list(list() for _ in range(n+1)) # 가중치를 저장할 그래프

for _ in range(m): # 모든 간선 정보를 입력받기
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e9) 
level = [INF]*(n+1) # 최단 거리 테이블을 모두 무한으로 초기화

q = []
heappush(q, (0, 1)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
level[1] = 0

while q: 
    clv, cur = heappop(q) 
    
    if level[cur] != clv: 
        continue
    
    for nxt, lv in graph[cur]:
        nlv = max(clv, lv) # 올때까지 가장 레벨이 높은 것만 고려하면 됨으로 이렇게 갱신
        if nlv < level[nxt]: 
            level[nxt] = nlv
            heappush(q, (nlv, nxt))

def isPrime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True 

for i in range(level[n]+1,int(1e9)): # level[n] 미만은 출입 불가이므로, 초과하는 최소한의 소수를 출력
    if isPrime(i):
        print(i)
        break
        
