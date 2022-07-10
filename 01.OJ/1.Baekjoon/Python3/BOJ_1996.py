# 1996 프린터 큐
# https://www.acmicpc.net/problem/1966
'''
1. 아이디어
- 문제의 설명을 따라 구현
- 주석 참고
2. 복잡도
- 주어진 문서의 길이 시간 복잡도
3. 자료구조
- 큐
'''
from collections import deque

def sol1966():
    tc = int(input())

    for _ in range(tc):
        n,m = map(int,input().split())
        docs = deque(list(map(int,input().split())))
        out_num=0

        while docs:
            doc_top = max(docs) # 중요도가 제일 높은 문서
            doc_1 = docs.popleft() # 가장 앞에 있는 문서
            m-=1 # 찾으려는 문서가 출력될 때까지, 왼쪽으로 이동하면서 탐색

            if doc_top == doc_1: # 가장 앞에 있는 문서가 중요도가 제일 높은 문서이면
                out_num+=1
                if m < 0: # 찾으려는 문서가 중요도가 제일 높은 문서라 출력
                    print(out_num)
                    break
            else:# 2. 가장 앞에 있는 문서가 중요도가 제일 높은 문서가 아니라면
                docs.append(doc_1) # Queue의 가장 뒤에 재배치
                if m<0: # 찾으려는 문서가 중요도가 제일 높은 문서가 아니면서 가장 앞에 있어
                    m = len(docs) - 1 # 가장 뒤에 재배치