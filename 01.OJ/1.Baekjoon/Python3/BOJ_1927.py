'''
 * 1927 최소 힙
 * https://www.acmicpc.net/problem/1927
 1. 아이디어
 - 
 - 
 2. 복잡도
 - 
 
 3. 자료구조
 -
'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
heap_length = 0

for _ in range(n):    # 1. 배열에 자연수 x를 넣는다.
    x = int(input())
    if x == 0:    # x가 0이라면
        if heap_length == 0:    # 배열이 비었으면 0 출력
            print(0)
        else:    # 있는 경우, 가장 작은 값 출력
            print(heapq.heappop(heap))
            heap_length = len(heap)
    else:
        heapq.heappush(heap, x)
        heap_length = len(heap)