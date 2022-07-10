# 10872 팩토리얼
# https://www.acmicpc.net/problem/10872
'''
1. 아이디어
- n!을 출력한다.
- n!=n*(n-1)*(n-2)*...*1
2. 복잡도
- O(n)
3. 자료구조
- 
'''
def sol10872():
    def f(n):
        if n==0:
            return 1
        else:       
            return n*f(n-1)
    print(f(int(input())))