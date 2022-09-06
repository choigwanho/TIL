'''
# [BOJ_1037 약수 -Python3](https://www.acmicpc.net/problem/1037)

## 문제분석
```Python
1. 관찰
- 양수 A가 N의 진짜 약수가 되려면, 
- N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
- 어떤 수 N의 진짜 약수가 모두 주어질 때, 
- N을 구하는 프로그램을 작성하시오.

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
import sys 
si = sys.stdin.readline

TOTAL = int(si()) # 약수의 개수
nums = list(map(int,si().split())) # 약수 리스트
print(max(nums)*min(nums))



