'''
* 11279 최대 힙
* https://www.acmicpc.net/problem/11279
1. 아이디어
- -x 로 heappush 하여 최대 힙을 만들어서 출력한다
2. 복잡도
- O(logn) 복잡도로 출력, O(n)회
3. 자료구조
- max heap
'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
heap_length = 0

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap_length == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))    # -x 로 추가하여 -를 붙여 출력
            heap_length = len(heap)
    else:
        heapq.heappush(heap, -x)    # 힙에 원소를 추가할 때 -x로 추가 하여 최대값 정렬
        heap_length = len(heap)