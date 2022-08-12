'''
# 프로그래머스 코딩테스트 실전 대비 모의고사 1차 - 1번  -Python3

## 문제분석
```Python
1. 관찰
- 두 정수 X, Y 에서 공통으로 나타나는 정수를 중복을 포함해서 찾는다.
- 찾은 수로 만들 수 있는 가장 큰 정수를 구한다.

- 공통 수가 없는 경우 -1
- 공통 수가 0만 있는 경우 0
- 이외의 경우 내림차순으로 정렬하여 가장 큰수를 만든다.


2. 복잡도
- 

3. 자료구조
-

```

## 해결코드
```Python
'''

def solution(X, Y):
    ans = []

    for s in list(set(X)&set(Y)): # 교집합
        xc = X.count(s)
        yc = Y.count(s)
        for _ in range(min(xc,yc)): # 적은 개수만큼 더하기
            ans.append(s)

    if not ans:# 공통이 되는 수가 없는 경우 
        return '-1'
    if max(ans) == '0':# 공통이 되는 수가 0만 있는 경우 
        return '0'
    
    ans.sort(reverse = True) # 내림차순 정렬하여 가장 큰수로 출력
    return "".join(ans)