'''
# 프로그래머스 코딩테스트 실전 대비 모의고사 3차 - 3번  -Python3


## 문제분석
```Python
1. 관찰


2. 복잡도

3. 자료구조


```

## 해결코드
```Python
'''
def solution(distance, scope, times):
    answer = 0
    t = [0]*(distance+1)
    for i in range(len(scope)):
        for s in range(scope[i][0],scope[i][1]+1):
            time= s%(times[i][0]+times[i][1])
            if 0 < time <= times[i][0]: # 근무시간
                t[s] = 1
    for i in range(1,distance+1):
        if t[i]==1:
            answer=i  
            break
            
    if answer==0:
        answer=distance

    return answer

# solution(10,[[3,4],[5,8]],[[2,5],[4,3]])
solution(12,[[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]])

