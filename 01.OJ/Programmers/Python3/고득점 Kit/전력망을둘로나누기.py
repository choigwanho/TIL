'''
n: 100 개의 송전탑 
wires: 99개의 전선 정보

트리 형태임으로 
n은 노드의 개수
wires은 간선의 개수이다

'''

def solution(n, wires):
    answer = -1
    tree = [[] for i in range(n+1)]
    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])


    for i in range(n+1):
        print(tree[i])

    return answer

testcase = [[9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]],
            [4,	[[1,2],[2,3],[3,4]]],
            [7,	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]]]

for n, wires in testcase:
	print(solution(n, wires))