'''
# [BOJ_1037 약수 -Python3](https://www.acmicpc.net/problem/1037)

## 문제분석
```Python
1. 관찰
- 유클리드 호제법 풀이

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))