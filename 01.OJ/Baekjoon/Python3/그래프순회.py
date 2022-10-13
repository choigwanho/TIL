'''

'''
from collections import deque

def findCycle(arr,cat):
    cat_cycle = []
    q = deque([cat])
    cat_cycle.append(cat)
    while q:
        now = q.popleft() 
        nxt = arr[now]

        if nxt-1 in cat_cycle: # 사이클임
            return cat_cycle

        if nxt-1 not in cat_cycle:
                cat_cycle.append(nxt-1)
                q.append(nxt-1)
    
def soloution(cycle, m):
    return findCycle(cycle, 0)

testcase = [[[2, 4, 1, 5, 3], 8],
            [[2, 4, 5, 4, 3], 12],
            [[5, 4, 2, 2, 4], 60],
            [[3, 1, 4, 2, 4], 120],
            [[6, 5, 9, 5, 3, 4, 8, 5, 1], 600],
            [[2, 4, 6, 8, 10, 1, 3, 5, 7, 9], 1150]]

for cycle, m in testcase:
    print(soloution(cycle, m))
