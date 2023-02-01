# 14426번 접두사 찾기
'''
5 10
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
star
start
code
sunday
coding
cod
online
judge
plus
'''

import sys
si = sys.stdin.readline

n, m = map(int, si().split()) # 문자열의 개수
trie = Trie()
s = [si() for _ in range(n)] # n개의 문자열로 이루어진 집합
t = [si() for _ in range(m)] # 검사해야 하는 m개의 문자열

# m개의 문자열 중에서 집합 s에 포함되어 있는 문자열 중 적어도 하나의 접두사인 것의 개수를 출력
