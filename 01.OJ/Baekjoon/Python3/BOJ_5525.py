"""
# [BOJ_5525 IOIOI](https://www.acmicpc.net/problem/5525)
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	18830	5617	4548	31.344%

문제
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

출력
S에 PN이 몇 군데 포함되어 있는지 출력한다.

제한
1 ≤ N ≤ 1,000,000
2N+1 ≤ M ≤ 1,000,000
S는 I와 O로만 이루어져 있다.

서브태스크
번호	배점	제한
1	50	
N ≤ 100, M ≤ 10 000.

2	50	
추가적인 제약 조건이 없다.

예제 입력 1 
1
13
OOIOIOIOIIOII
예제 출력 1 
4
OOIOIOIOIIOII
OOIOIOIOIIOII
OOIOIOIOIIOII
OOIOIOIOIIOII
예제 입력 2 
2
13
OOIOIOIOIIOII
예제 출력 2 
2
OOIOIOIOIIOII
OOIOIOIOIIOII


sol 1)
## 문제 분석
1. 관찰
- N이 주어졌을때
- N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열 Pn
- 길이 M짜리 S안에 Pn이 몇군데 포함되어 있는지 구하여라

P1 = IOI
P2 - IOIOI
p3 = IOIOIOI
...

Pn은 2*N+1 의 길이이고 홀수 번째에 I 짝수번째에 O 규칙을 갖는다.
N에 따른 Pn을 만들어 주고

S에서 2*N+1길이를 순서대로 모두 비교한다.


2. 복잡도
- O(N+M) = 1000000 + 1000000 >> 2백만 가능

3. 자료구조
- 문자열


sol 2) 
## 문제 분석
1. 관찰
- Pn에는 n+1개의 I, 2의 거리로 존재
- S에서 Pn을 셀 때 I의 거리가 중요
- Pn을 판단하는 방법으로
- S에서 I의 거리가 2인 경우가 연속적으로 N번 이상이면 P임을 알 수 있다.


2. 복잡도
- O(S에서 I의 개수)

3. 자료구조
- I의 인덱스 리스트 : int[] 

"""

import sys
si = sys.stdin.readline

N = int(si())
M = int(si())
S = si().strip()

i_index = [i for i in range(M) if S[i]=="I"]
cnt = 0
ans = 0

for i in range(0,len(i_index)): # "I"가 2간격으로 N번 연속적인 경우 완전 탐색 
    if i_index[i] - i_index[i-1] == 2:
        cnt += 1
    else: # I와 I의 거리가 2가 아닌경우 끊어준다.
        cnt =0
    if cnt >= N:
        ans += 1
print(ans)