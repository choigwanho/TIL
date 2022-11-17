'''
# [BOJ_1922 네트워크 연결 -Python3](https://www.acmicpc.net/problem/1922)

## 문제분석
```Python
1. 관찰

- 배경지식 빌드업
- 서로소 집합 -> 유니온 파인드 -> 크루스칼

- 신장트리: 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
  - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 함
  - 사이클이 존재하면 신장트리가 아님

- 최소한의 비용으로 구성되는 신장 트리를 찾아야 할 때
- N개의 노그가 존재하는 상황에 두 노드에 간선을 놓아 전체 노드가 서로 연결될 수 있게 하는 도로를 설치하는 경우 
  - 두 노드를 선택했을 때 노드1에서 노드2로 이동하는 경로가 반드시 존재하도록 도로를 설치한다는 의미 

- 크루스칼 알고리즘
  - 그리디 알고리즘으로 분류

- 동작과정
  1. 간선 데이터를 비용에 따라 오름차순 정렬
  2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    2.1 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
    2.2 사이클이 발생하는 경우 최소 신창 트리에 포함시키지 않음
  3. 모든 간선에 대하여 2번 과정 반복


2. 복잡도
- O(ElogV + VlogV)

3. 자료구조
- 부모노드, 간선정보: int[]

```

## 해결코드
```Python
'''
def find_root(root, n):
  if root[n] != n:
    root[n] = find_root(root, root[n])
  return root[n]

def union_root(root, n1, n2):
  n1 = find_root(root, n1)
  n2 = find_root(root, n2)
  if n1 > n2:
    root[n1] = n2
  else:
    root[n2] = n1


import sys
si = sys.stdin.readline

n = int(si()) # o
m = int(si()) # v

root = [i for i in range(n+1)] # 사이클 판별을 위한 루트 리스트
v_list = [] # 간선 정보 저장 리스트

for _ in range(m):
  a, b, cost = map(int, si().split()) 
  v_list.append((cost, a, b))

v_list.sort() # 비용 기준 오름차순 정렬

ans = 0
for cost, n1, n2 in v_list:
  if find_root(root, n1) != find_root(root, n2): # 사이클을 생성하지 않으면
    union_root(root, n1,n2) # 서로소 집합에 추가
    ans += cost

print(ans) 