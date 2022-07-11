1. 힙(Heap) 이란?
- 일종의 트리
- 수의 집합에서 가장 작은 수(키)나 가장 큰 수만을 자주 꺼내올 때 유용한 자료구조
- 배열에서는 최소값 탐색시 O(n), 힙에서는 O(logn)으로 시간복잡도에서 유리

2. 힙의 구조
- 트리 중 완전 이진 트리
- 항상 자식은 두개 밖에 없다.
- leaf의 가장 왼쪽부터 채운다
- 키값의 대소 관계는 부모/자식 간에만 성립
- 형제노드 사이에는 대소 관계가 정해지지 않는다

3. 최소힙, 최대힙
- 최소힙: 가장 작은 값이 루트
- 최대힙: 가장 큰 값이 루트

4. 힙의 구현
- leftChild = parent*2
- rightChild = parent*2+1
- parent = child/2

5. 파이썬에서 heapq 모듈 사용
- import heapq : 파이썬 heapq 모듈은 heapq (prirority queue) 알고리즘 제공

6. 힙 함수 활용하기
- heapq.heappush(heap, iteam): item을 heap에 추가
- heapq.heappop(heap): heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
- heapq.heapify(x): 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N))

- 참조
- https://reakwon.tistory.com/42
- https://littlefoxdiary.tistory.com/3
