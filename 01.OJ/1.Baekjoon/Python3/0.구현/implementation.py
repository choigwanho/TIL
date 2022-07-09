# https://www.acmicpc.net/problemset?sort=ac_desc&algo=102
# 실버 5이상 위주로 다 풀기

from email.utils import localtime
from logging.config import valid_ident
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

# 2750 수 정렬하기
# https://www.acmicpc.net/problem/2750
'''
1. 아이디어
- 중복되지 않는 N개의 수를 오름차순으로 정렬한다.
2. 복잡도
- sort() 리스트 내장함수
3. 자료구조
- 크기 n 짜리 리스트
*추가
sorted()는 새로운 정렬된 리스트 반환
sort는 기존 리스트에 정렬(in-place)
참조: https://docs.python.org/ko/3/howto/sorting.html
'''
def sol2750():
    n=int(input())
    nums=list(int(input().rstrip()) for _ in range(n))

    for n in sorted(nums):
        print(n)

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

# 2558 A+B - 2
def sol2558():
    a= int(input())
    b =int(input())
    print(a+b)
    
# 15596 정수 N개의 합
# https://www.acmicpc.net/problem/15596
def solve(a):
    ans = sum(a)
    return ans

# 10817 세 수
def sol10817():
    nums =list(map(int,input().split()))
    nums.sort()
    print(nums[1])
    
# 2440 별 찍기 - 3
def sol2440():
    n = int(input())
    for i in range(n,0,-1):
        print("*"*i)
    print()

# 1316 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
'''
1. 아이디어
- 다음 문자와 서로 다를 때, 그 뒤에 현재 문자가 있으면 그룹단어에서 제외
2. 복잡도
- len(word) 상수 복잡도
3. 자료구조
- 리스트
'''
def sol1316():
    n = int(input())

    for _ in range(n):
        word = input().strip()

        for i in range(len(word)-1):
            if word[i]!=word[i+1]:
                if word[i] in word[i+1:]:
                    n-=1
                    break
    print(n)
    
# 7287 등록
def sol7287():
    print(59)
    print('rhksghsss')

# 5622 다이얼
'''
1. 아이디어
- 3으로 나누어 알파벳 그룹을 나누려고 보니, 7과 9는 4글자씩 있다.
- 알파벳 리스트를 만들어서 직접 비교
2. 복잡도
- word의 길이 시간 복잡도
3. 자료구조 
- 리스트
'''
def sol5622():
    alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    word = input()

    time =0 
    for unit in alpabet_list:
        for i in unit:
            for x in word:
                if i == x:
                    time += alpabet_list.index(unit) + 3

    print(time)

# 2941 크로아티아 알파벳
def sol2941():
    alpabet_list=['c=','c-','dz=','d-','lj','nj','s=','z=']
    word=input().strip()
    cnt=0

    for alpabet in alpabet_list:
        for i in range(len(word)-len(alpabet)+1):
            if alpabet == word[i:i+len(alpabet)]:
                cnt+=1
        word = word.replace(alpabet," ")
    word= word.replace(" ","")

    print(len(word))
    print(cnt+len(word))

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