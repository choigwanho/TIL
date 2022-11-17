'''
# [BOJ_16917 양념 반 후라이드 반 -Python3](https://www.acmicpc.net/problem/16917)

## 문제분석
```Python
1. 관찰
-

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
a, b, c, x, y = map(int, input().split())

if a + b < 2 * c:
    print(a * x + b * y)
else:
    print(2 * c * min(x, y) + min(a, 2 * c) * max(0, x - y) + min(b, 2 * c) * max(0, y - x))