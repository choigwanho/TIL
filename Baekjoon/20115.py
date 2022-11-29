# [BOJ_20115 에너지 드링크](https://www.acmicpc.net/problem/20115)

## 문제 분석
"""
1. 관찰
- 최대로 만들 수 있는 에너지 드링크의 양은
- 직관적으로 가장 큰 값을 a로 선택하고 나머지 음료들의 절반을 다 더한 값과 같음을 알 수 있다.

2. 복잡도
- max() = O(N)
- sum() = O(N)
>> 100000 + 100000 >> 가능

3. 자료구조
- int

"""
## 해결 코드
import sys
si = sys.stdin.readline

N = int(si())
drinks = list(map(int, si().split()))

M = max(drinks)
S = sum(drinks)

print(M+(S-M)/2)










