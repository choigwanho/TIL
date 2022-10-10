'''
# [Programmers] [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860) -Python3

## 문제분석
```Python
1. 관찰
- "A"*len(name) 상태에서 주어진 name을 만들기위해 조이스틱을 상하좌우로 움직이는 최소 횟수를 구해야한다.
- 상하로 움직이는 경우는 각 자리의 문자와 "A"의 유니코드 정수의 차이를 사용하여 최소 횟수를 구할 수 있다.
- 하지만, 좌우로 이동하는 경우는 A의 유무, A의 연속된 길이, A의 위치에 따라 움직임을 고려해 주어야 하기 때문에 이를 고려하여 최소 움직임을 구해야한다.

- 다른 풀이들을 참고하였지만, 좌측으로 움직임, 우측으로 움직임을 수식으로 정리하여 최소 값을 구하는 방식이 직관적으로 이해가 되지 않았다.
- 따라서, 좌우 이동의 최소횟수를 구하기 위해서 최단거리를 구하는데 일반적으로 사용되는 BFS 알고리즘으로 접근하였다.

-  "A"*len(name)에서 주어진 name을 만들기 위해 A가 아닌 곳을 바꾸기위해 최소로 움직이며 모두 방문하여 주어진 name과 일치하도록 만들어주어야한다.
- 역으로, 주어진 name이 모두 A가 되게하는 최소 이동거리를 구해준다.

- name이 "A"*len(name)이 될 때까지 BFS를 해주며 좌우로 이동한 거리를 누적해준다.
- 이때, "A"*len(name)을 가장 빨리 만족하는 경우를 찾기위해 deque에 현재 name 의 상태를 deepcopy하여 기록해나가야한다.

2. 복잡도
- O(len(name) + len(name)) = 20 + 20 = 40
- 검토 필요

3. 자료구조
- 이름: str[]
- BFS: deque

```

## 해결코드
```Python
'''

from collections import deque
from string import capwords

def bfs(name):
    q = deque([(list(name), 0, 0)])

    while q:
        name_list, lr_cnt, idx = q.popleft()
        name_list[idx]='A'

        if name_list.count('A') == len(name):
            return lr_cnt
        
        for i in [-1,1]:
            name_copy = name_list[:]
            q.append((name_copy, lr_cnt+1, idx+i))

def solution(name):
    up_cnt = sum([min(abs(ord('A')-ord(n)), 26-abs(ord('A')-ord(n))) for n in name])
    lr_cnt = bfs(name)
    print("lr_cnt : ", lr_cnt)
    return up_cnt + lr_cnt


testcase = ["DYAOAAAARQANAWA"]
for name in testcase:
    print("len of name: ",len(name))
    print(solution(name))


"AAABABAAAB", ["AAB","AA","AAB","BAA"] 

AAABABAAAB
idx

dp = [r len(0 fostring)+1]

while q:
    for i range(idx+1, len())
    idx:i in words:

cards 1,2, 3 343
패턴 [2,1,5,]

i, v enumarate(패턴)
최소값 
