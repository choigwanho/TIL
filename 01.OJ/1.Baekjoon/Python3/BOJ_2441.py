# [BOJ_2441 별 찍기 - 4 - Python3](https://www.acmicpc.net/problem/2441)
'''
1. 아이디어
- .rjust(n,"") 로 우측정렬, 왼쪽 채우기
2. 복잡도
- O(n) loop
3. 자료구조
- 문자열
'''

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n,0,-1):
    star="*"*i
    print(star.rjust(n," "))