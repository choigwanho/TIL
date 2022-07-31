
import sys
input = sys.stdin.readline

# 2750 수 정렬하기
# https://www.acmicpc.net/problem/2750
'''
1. 아이디어
- 중복되지 않는 N개의 수를 오름차순으로 정렬한다.
2. 복잡도
- sort() 리스트 내장함수
3. 자료구조
- 크기 n 짜리 리스트
*추가
sorted()는 새로운 정렬된 리스트 반환
sort는 기존 리스트에 정렬(in-place)
참조: https://docs.python.org/ko/3/howto/sorting.html
'''
def sol2750():
    n=int(input())
    nums=list(int(input().rstrip()) for _ in range(n))

    for n in sorted(nums):
        print(n)