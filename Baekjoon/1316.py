# 1316 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
'''
1. 아이디어
- 다음 문자와 서로 다를 때, 그 뒤에 현재 문자가 있으면 그룹단어에서 제외
2. 복잡도
- len(word) 상수 복잡도
3. 자료구조
- 리스트
'''

import sys
input = sys.stdin.readline

def sol1316():
    n = int(input())

    for _ in range(n):
        word = input().strip()

        for i in range(len(word)-1):
            if word[i]!=word[i+1]:
                if word[i] in word[i+1:]:
                    n-=1
                    break
    print(n)