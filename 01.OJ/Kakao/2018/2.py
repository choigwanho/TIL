import re

def solution(dartResult):
    p = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    answer = []
    cal = {
        'S':lambda x:x,
        'D':lambda x:x**2,
        'T':lambda x:x**3
    }
    for n, op, win in p.findall(dartResult):
        score =0
        if op =='S':
            score = cal['S'](int(n))
        elif op=='D':
            score = cal['D'](int(n))
        elif op=='T':
            score = cal['T'](int(n))
        
        if win=='*':
            score *= 2
            if answer:
                answer[-1] *=2
        elif win=='#':
            score*=-1
        answer.append(score)
    return sum(answer)

testcase = ['1S2D*3T'] 

for t in testcase:
    print(solution(t))