import sys
input = sys.stdin.readline

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