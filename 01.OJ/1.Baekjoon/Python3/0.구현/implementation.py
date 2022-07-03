# https://www.acmicpc.net/problemset?sort=ac_desc&algo=102
# 실버 5이상 위주로 다 풀기

import sys
input = sys.stdin.readline

# 4673 셀프 넘버
'''
1. n과 n의 자리수를 더하는 재귀함수를 만든다.
2. 1 ~ 10,000까지 만들어진 수 리스트를 만든다.
3. for loop로 만들어지지 않은 수를 출력한다.
'''
def sol4673():
    nums=[]
    for i in range(1,10001):
        nums.append(i)
    

        

    for i in range(1,10001):
        if i not in nums:
            print(i)

sol4673()