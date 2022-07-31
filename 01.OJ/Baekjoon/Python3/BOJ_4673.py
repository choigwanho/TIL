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