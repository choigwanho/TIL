'''
k가 0.1초당 p배씩 증가할 때, n초 후에 k마리는 총 몇 마리가 되는지 구하는 문제

k는 1억, p는 1억, n는 1억*1억
'''
# sol 1 - 분할 정복
import sys
si = sys.stdin.readline

# 지수를 재귀적으로 나누는 함수, 분할 정복
def f(x, y):
    if y == 1:
        return x
    elif y % 2 == 0:
        a = f(x, y / 2)
        return a * a % 1000000007
    else:
        b = f(x, (y - 1) / 2)
        return b * b * x % 1000000007

k, p, n = map(int, si().split()) # 처음 바이러스의 수 k, 증가율 p, 총 시간 n(초)

exponent = f(p, 10*n) # 지수를 재귀적으로 나눈 값
print(k* exponent % 1000000007)

# sol 2 - pow(밑, 지수, 나누는 값) -> 밑의 지수승을 나누는 값으로 나눈 나머지
import sys
si = sys.stdin.readline
k, p, n = map(int, si().split()) # 처음 바이러스의 수 k, 증가율 p, 총 시간 n(초)
print(k*pow(p,n*10,int(1e9+7))%int(1e9+7))
