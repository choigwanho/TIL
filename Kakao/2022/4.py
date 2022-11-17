from collections import deque
from math import ceil

def solution(numbers):
    answer = []

    for n in numbers:
        n = bin(n)[2:]
        l = len(n)
        if l%2==0:
            n=n.zfill(l+1)

        cnt=0

        if n[len(n)//2]=='0':
            answer.append(0)
            continue
        else:
            cnt=1

        mid = len(n)//2
        for i in range():
            for nxt in [mid-ceil(mid/2),mid+ceil(mid/2)]:
                if 0<=nxt<len(n):
                    if '1' == n[nxt]:
                        cnt+=1

        if n.count('1')==cnt:
            answer.append(1)
        else:
            answer.append(0)
    return answer

testcase =[
    [7, 5],
    [63, 111, 95]
]

for case in testcase:
    print(solution(case))