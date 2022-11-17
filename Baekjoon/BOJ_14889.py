'''
# [BOJ_14889 스타트와 링크 -Python3](https://www.acmicpc.net/problem/14889)

## 문제분석
```Python
1. 관찰
- 스타트링크 축구 모임 
- 평일 오후 
- 참석은 0 1 선택
- N명 참석, N%2 ==0 짝수
- N/2 명으로 이루어진 스타트 팀과 링크 팀으로 팀을 나눈다.
- 사람에게 번호 부여 1~N

- N//2 명을 뽑는다.

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

def dfs(depth, idx):
    global ans
    # n//2 인 경우 두 팀의 차이를 계산하여 갱신
    if depth == n//2:
        p1, p2 = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    p1+=graph[i][j]
                elif not visited[i] and not visited[j]:
                    p2+=graph[i][j]
        ans =  min(ans, abs(p1-p2))
        return
    
    # n//2 명을 뽑는 모든 경우 dfs 탐색
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0

n = int(si())

visited = [0 for _ in range(n)]
graph = list(list(map(int,si().split()))for _ in range(n))
ans = int(1e9)

dfs(0,0)
print(ans)