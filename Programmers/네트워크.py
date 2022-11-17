from collections import deque
def solution(n, computers):
    answer = 0
    network = [[] for _ in range(len(computers)+1)]
    check = [0 for _ in range(len(computers)+1)]
    for i, computer in enumerate(computers):
        for j, v in enumerate(computer):
            if v==1:
                network[i+1].append(j+1)
                
    def dfs(node):
        q = deque()
        q.append(node)
        while q:
            n = q.popleft()
            for i in network[n]:
                if not check[i]:
                    check[i]=1
                    q.append(i)

    for i in range(1, len(computers)+1):
        if not check[i]:
            dfs(i)
            answer+=1

    return answer

solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
#solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]])

