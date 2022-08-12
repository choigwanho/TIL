'''
# 프로그래머스 코딩테스트 실전 대비 모의고사 1차 - 2번  -Python3

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
from collections import defaultdict
def solution(want, number, discount):
    wl = len(want)
    nl = sum(number) 
    dl = len(discount)

    hm = defaultdict(int) # 과일명: 숫자, 해쉬맵을 만든다.
    for i in range(wl):
        hm[want[i]] =  number[i]

    answer = 0
    for i in range(dl-nl+1): 
        dc = discount[i:i+nl]
        cnt =0
        for w in want: 
            if hm[w] == dc.count(w):
                cnt += 1
        if cnt == len(want): # 모두 만족하면
            answer += 1
    return answer