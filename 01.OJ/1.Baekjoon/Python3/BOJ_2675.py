# 2675 문자열 반복
def sol2657():
    n = int(input())
    case=[]
    s=""
    for _ in range(n):
        tmp = list(map(str,input().split()))
        
        for c in tmp[1]:
            s += int(tmp[0])*c
        case.append(s)
        s=""

    for v in case:    
        print(v)