'''
# [BOJ_1068 트리 -Python3](https://www.acmicpc.net/problem/1068)

## 문제분석
```Python
1. 관찰
- 타겟노드부터 하위노드 삭제
    - 현재 노드 위치에 부모노드 값을 갖는다.
    - 따라서, 타겟 노드를 지우고
    - 타겟 노드를 부모노드로 가지고 있는 하위 노드들을 지우는 것을 반복하여 삭제한다.

- 리프노드 카운팅
    - 삭제되지 않은 노드에 대하여
    - 자기 자신을 부모노드로 가리키고 있는 노드가 없으면 카운팅

2. 복잡도
- O()

3. 자료구조
- tree : int[]

```

## 해결코드
```Python
'''

def dfs(node):
    tree[node] = -2 # 현재 노드 삭제 처리, (root 노드 0(-1)과 구분을 하기 위해 -2로 처리)
    for i in range(n): 
        if node==tree[i] : # 현재노드를 부모로 갖는 노드(하위노드)에 대해  dfs 하여 삭제 처리
            dfs(i)

import sys
si = sys.stdin.readline

n = int(si()) # 노드의 개수
tree = list(map(int,si().split()))
target= int(si())

dfs(target)
cnt_leaf = 0
for i in range(n):
    if tree[i] != -2 and i not in tree: # 삭제되지 않은 노드인 경우, 자신의 하위 노드없으면 리프노드
        cnt_leaf +=1
print(cnt_leaf)




