'''
* 11286 절댓값 힙
* https://www.acmicpc.net/problem/11286
1. 아이디어
- 절대값으로 묶어서 담는다.
2. 복잡도
- O(logn), O(n) 회
3. 자료구조
- heap
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
            print(heapq.heappop(heap)[1])    # (abs(x), x))에서 꺼내기 위해 [1]로 인덱싱
            heap_length = len(heap)
    else:
        heapq.heappush(heap, (abs(x), x))    # abs() 절대값 내장 함수로 xb플 형태로 heappush
        heap_length = len(heap)
