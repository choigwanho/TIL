'''
# [Programmers] [징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236) -Python3
## 문제분석
```Python
1. 관찰
- 맨 처음에는 n개를 지울 수 있는 모든 경우를 조합으로 구하여
모든 케이스에 대한 가장 작은 차이값 중 가장 큰 값을 출력하는 방식으로 접근했다.
- 하지만, 문제에서 주어진 것처럼 바위의 개수는 5만개이며 시작과 끝의 차이는 10억이다.

  - 5만개의 바위에서 n개를 제거한 조합을 찾는 시간복잡도는 5만이며
모든 케이스의 차이값을 탐색하기위해서는 5만*5만 이상이 소요된다. 
  - 따라서, 이 문제는 완전 탐색으로 접근하면 효율성 TC에 의해서 통과하지 못한다.

- 시간 복잡도를 개선하기위해서 이분탐색으로 문제를 접근해본다.
- 이분탐색으로 접근하게된다면 10억도 30번이면 탐색이 가능하고, 5만은 16번이면 탐색가능하다.

- 그래서, 어떻게 풀이를 해야하나?

- 우리가 찾는 값은 바위 n개를 제거했을 때 각 바위 사이의 거리를 측정하여 나온 최소거리 중에서 최대값이다.
- 따라서, 이분 탐색으로 찾는 값을 바위를 지우기 위한 최소 간격으로 설정하고 문제를 접근해 보아야 한다.

- 투 포인터를 통해 최소간격보다 작은 경우 해당 바위를 지운다. (시간복잡도 : len(rocks) => 5만)

- 지워진 바위의 개수가 n보다 크면 상한값을 축소(최소 간격을 감소)시키고,
- 지워진 바위의 개수가 n이하이면 하한값을 축소(최소 간격을 증가)시킨다. 

- 그렇게 n개를 지우는 경우에 대하여 low와 high가 같아질 때 까지 이분탐색을 반복해주면 mid 값은 n개를 제거하는 최소간격 중 최대값을 만족한다.

2. 복잡도
- O(log2(dis)*rocks) = 16*5만 => 약 90만
- 이분탐색을 통해 가능

3. 자료구조
- 바위 거리 : int[]
- n개를 제거하는 간격: int

```

## 해결코드
```Python
'''

def solution(distance, rocks, n):

    answer = 0
    rock_list = sorted(rocks) + [distance] # 50,000

    low = 0
    high = distance
    idx=0

    while low <= high: # log2(50,000) = 약 16
        mid = (low+high)//2
        current = 0
        remove = 0 
        
        idx += 1
        for rock in rock_list:
            diff = rock - current 
            if diff >= mid:
                current = rock
            else:
                remove += 1
                
        if remove > n:
            high = mid -1
        else:
            low = mid + 1 
            answer = mid 

    return answer