'''
# 프로그래머스 코딩테스트 실전 대비 모의고사 2차 - 1번  -Python3

## 문제분석
```Python
1. 관찰
- 학생들 각각 정수 번호
- 학생 3명 번호 합 0 이면 삼총사
- 삼총사를 만드는 경우의 수를  출력

2. 복잡도
- O(nP3) = n 조건이 기억이 안남 >> 가능

3. 자료구조
- answer: int

```

## 해결코드
```Python
'''

# [-2,3,0,2,-5]
# [-3,-2,1,0,1,2,3]
# [-1,1,-1,1]
def solution(number):
    end = len(number)
    answer = 0
    for i in range(end):
        for j in range(i+1,end):
            for k in range(j+1,end):
                if number[i]+number[j]+number[k] == 0:
                    print(number[i],number[j],number[k])
                    answer+=1
    return answer
    

# 시간 초과 코드 -> 메모이제이션 ? 관련해서 개선하면 풀 수 있는지 확인하고 싶음
'''
answer = 0
def solution(number):
    memo=[]
    check = [0 for _ in range(len(number))]
    
    def recur(chosen):
        global answer
        if len(chosen)==3 and sum(chosen)==0:
            answer +=1
            print(check,answer)
            return

        for i in range(len(number)):
            if not check[i]:                                          
                check[i]=1
                chosen.append(number[i])
                recur(chosen)
                chosen.pop()
                check[i]=0

    recur([])
    return answer//6

solution([-2,3,0,2,-5])
'''