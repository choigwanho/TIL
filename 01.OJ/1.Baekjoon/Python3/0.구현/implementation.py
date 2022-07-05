# https://www.acmicpc.net/problemset?sort=ac_desc&algo=102
# 실버 5이상 위주로 다 풀기

import sys
input = sys.stdin.readline

# 4673 셀프 넘버
'''
1. 아이디어
- n과 n의 자리수를 더하는 재귀함수를 만든다.
- 1 ~ 10,000까지 만들어진 수 리스트를 만든다.
- for loop로 만들어지지 않은 수를 출력한다.
2. 복잡도
3. 자료구조
'''
# set은 교집합, 합집합, 차집합 구할 때 많이 사용
def sol4673():
    not_self_num = []

    def d(n):
        sum = n
        for i in str(n):
            sum +=int(i)
        return sum

    for i in range(1,10001):
        not_self_num.append(d(i)) 

    for i in range(1,10001):
        if i not in not_self_num:
            print(i)




# 1475 방 번호
# https://www.acmicpc.net/problem/1475
'''
1. 아이디어
- 같은 숫자가 중복인 횟수만큼 세트가 필요하다.
- 6혹은 9가 있는 경우 한 세트로 2개를 커버가 가능하다.
- 6과 9가 동시에 있는 경우 많이 있는 경우는 max(cnt_list)로 처리 가능
2. 복잡도
- 
3. 자료구조
- set()
'''
def sol1475():
    n = input()
    cnt = [0]*9
    for x in n:
        ind = int(x)
        if ind==9:
            ind =6
        cnt[ind] +=1
    cnt[6]=(cnt[6]+1)//2
    print(max(cnt))

