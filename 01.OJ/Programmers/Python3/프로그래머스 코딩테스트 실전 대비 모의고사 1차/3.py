'''
# 프로그래머스 코딩테스트 실전 대비 모의고사 1차 - 3번  -Python3

## 문제분석
```Python
1. 관찰
-

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
from collections import deque
def solution(order):
    Q = deque() # 오름차순 리스트
    for i in range(1,len(order)+1):
        Q.append(i)

    st = deque() # 컨테이너 벨트 리스트
    cnt =0

    while Q: # 순서대로 비교
        if order[cnt] != Q[0]: # 오름차순과 순서가 다를때
            if st and order[cnt] == st[-1]: # 컨테이너벨트에 값이 있고 탐과 순서가 같으면 
                cnt +=1
                st.pop() # 출력
            else: 
                st.append(Q.popleft()) # 컨테이너 벨트에 싣는다.
        else: # 같으면 출력
            cnt += 1
            Q.popleft()

    while st: # 큐가 비었으면 스택의 탑이 order 순서가 다른게 나올때까지 돌린다.
        if order[cnt] == st[-1]:
            cnt += 1
            st.pop()
        else:
            break
    return cnt
