'''
# [BOJ_9370 미확인 도착지 -Python3](https://www.acmicpc.net/problem/9370)

## 문제분석
```Python
0. 다익스트라(Dijkstra) 알고리즘
- 다이나믹 프로그래밍을 활용한 대표적인 최단경로(Shortest Poth) 탐색 알고리즘
- 특정한 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 확인할 수 있음

- 다익스트라 알고리즘이 다이나믹 프로그래밍인 이유
  - 최단 거리는 여러 개의 최단 거리롤 이루어져 있기 때문
  - 하나의 최단 거리를 구할 때 그 이전가지 구했던 최단 거리 정보를 그대로 사용하는 특징이 있음
  - 현재까지 알고 있던 최단 경로를 계속해서 갱신

- 다익스트라 알고리즘 동작 과정
    1. 출발 노드 설정
    2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장
    3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드 선택
    4. 해당 노드를 거쳐서 특정한 노드로 가능 경우를 고려하여 최소 비용을 갱신
    5. 위 과정 반복

- 이차원 배열 형태로 그래프 처리
- 특정 행에서 열로 가능 비용을 그래프로 만듦

- sol1. 선형 탐색 O(N**2)

- sol2. 인접 리스트 방식 O(N*logN)

- 

1. 관찰
- B100 요원에 몰입해서 풀어본다.

- 예술가 한 쌍이 도시의 거리들을 이동한다.
- 그들이 어디로 가고 있는지 알아내는 임무이다.

- 우리가 아는 정보는 다음과 같다.
  - S지점에서 출발
  - 목적지 후보들 중 하나에 도착
  - 최단거리로 이동

- g와 h 교차로 사이에 있는 도로를 지나갔다.


2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
'''


def dijkstraByAdjacencyList(graph, start):
    distances = {node: int(1e9) for node in graph}
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [distances[start], start])

    while pq:
        current_distance, current_target = heapq.heappop(pq)
        if distances[current_target] < current_distance:
            continue
            
        for new_target, new_distance in graph[current_target].items():
            distance = current_distance + new_distance
            if distance < distances[new_target]:
                distances[new_target] = distance
                heapq.heappush(pq, [distance, new_target])

    return distances

import heapq
from collections import defaultdict
import sys
si = sys.stdin.readline

T = int(si())
for _ in range(T):
    n, m, t = map(int,si().split()) # 노드의 개수, 간선의 개수, 목적지의 개수
    s, g, h = map(int,si().split()) # 출발 노드, 지나간 두 노드

    graph = defaultdict(dict)
    for node in range(n+1): # 0(n) 2,000
        graph[node]
    for _ in range(m): # 0(n) 50,000
        a, b, d = map(int,si().split()) # 두 개의 노드와 그 사이 거리
        if (a == g and b == h) or (a == h and b == g):
            d -= 0.01
        graph[a][b] = d
        graph[b][a] = d

    # 목적지 리스트 초기화
    target_list = [int(si()) for _ in range(t)] # 0(n) 1,000

    s_distances = dijkstraByAdjacencyList(graph, s)
    answer = []
    for target in target_list:
        if isinstance(s_distances[target], float):
            answer.append(target)

    print(*sorted(answer))

'''

def dijkstraByAdjacencyList(graph, start):
    distances = {node: int(1e9) for node in graph}
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [distances[start], start])

    while pq:
        current_distance, current_target = heapq.heappop(pq)
        if distances[current_target] < current_distance:
            continue
            
        for new_target, new_distance in graph[current_target].items():
            distance = current_distance + new_distance
            if distance < distances[new_target]:
                distances[new_target] = distance
                heapq.heappush(pq, [distance, new_target])
    return distances

import heapq
from collections import defaultdict
import sys
si = sys.stdin.readline

T = int(si())
for _ in range(T):
    n, m, t = map(int,si().split()) # 노드의 개수, 간선의 개수, 목적지의 개수
    s, g, h = map(int,si().split()) # 출발 노드, 지나간 두 노드

    graph = defaultdict(dict)
    for node in range(n+1): # 0(n) 2,000
        graph[node]
    for _ in range(m): # 0(n) 50,000
        a, b, d = map(int,si().split()) # 두 개의 노드와 그 사이 거리
        graph[a][b] = d
        graph[b][a] = d

    # 목적지 리스트 초기화
    target_list = [int(si()) for _ in range(t)] # 0(n) 1,000

    s_distances = dijkstraByAdjacencyList(graph, s)


    gh_distance = graph[h][g]

    # 중복된 이동을 제거하기 위해 필수 통로 제거
    graph[g].pop(h)
    graph[h].pop(g)

    answer = []
    for target in target_list:
        target_distances = dijkstraByAdjacencyList(graph, target)
        if s_distances[target] >=  min(s_distances[g] + gh_distance + target_distances[h], s_distances[h] + gh_distance + target_distances[g]): # s-g-h-목적지 거리가 최단거리보다 작거나 같으면 가능
             answer.append(target)

    print(*sorted(answer))

