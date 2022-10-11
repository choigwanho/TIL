'''
# [Programmers] [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) -Python3

## 문제분석
```Python
1. 관찰
- 송전탑이 전선을 통해 하나의 트리(Tree) 형태로 연결되어 있다.
- 따라서 송전탑은 '노드', 전선은 '간선'으로 이해할 수 있다.

- 문제에서 요구하기를 전력망 네트워크를 2개로 분할하려고 한다.
- 주어진 간선의 개수가 99개 이하임으로 완전 탐색을 구현해도 된다.
  - wires 중 하나를 제거하면 네트워크가 2개로 분할되는 것을 이용해 완전 탐색을 한다.

- 2개로 분할된 모든 경우에 대하여 두 네트워크의 노드 개수를 비교하고 최소값을 출력한다.
  - 분할된 한 네트워크에 대하여 BFS하여 노드의 개수를 구한다.
  - 전체 노드의 개수 n을 사용하여 두 네트워크의 노드의 개수를 비교한다.

2. 복잡도
- O(V*(V+E)) =  99 * (99 + 100)  => 그냥 가능이다.
- 합리적으로 완전탐색을 시도할 수 있다.

3. 자료구조
- 트리: int[][]
- 방문 처리: int[]

```

## 해결코드
```Python
'''
from collections import deque
 
def bfs(tree, start, visited):
    q = deque([start])
    visited.append(start)
    while q:
        now = q.popleft()
        for nxt in tree[now]:
            if nxt not in visited:
                q.append(nxt)
                visited.append(nxt)
    return len(visited)

def solution(n, wires):

    answer = n

    for i in range(len(wires)):
        tree = [[] for _ in range(n)]
        for idx, wire in enumerate(wires):
            if idx==i:
                continue
            tree[wire[0]-1].append(wire[1]-1)
            tree[wire[1]-1].append(wire[0]-1)
        
        one = bfs(tree, 0, [])

        result = abs((n - one) - one)

        if answer > result:
            answer = result

    return answer