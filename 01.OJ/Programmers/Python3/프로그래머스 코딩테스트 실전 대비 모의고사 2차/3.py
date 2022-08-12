'''
# 프로그래머스 코딩테스트 실전 대비 모의고사 2차 - 3번  -Python3

## 문제분석
```Python
1. 관찰

- 지역은 유일한 번호로 구분된다.
- 거리 1로 동일
- 최단시간으로 부대 복귀
- 적군-> 돌아오는 경로가 없어질 수 있다.

- 그래프 
- 트리


2. 복잡도
- 

3. 자료구조
-

```

## 해결코드
```Python
'''


def solution(n, roads, sources, destination):

    answer = []
     
    graph = [0 for _ in range(n+1)]

    for road in roads:
        graph[road[0]].appned(road[1])
        graph[road[1]].appned(road[0])

    return answer