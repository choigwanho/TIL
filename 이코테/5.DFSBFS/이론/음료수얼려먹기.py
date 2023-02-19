import sys
si = sys.stdin.readline

n, m = map(int,si().split())

graph = []
for i in range(n):
    graph.append(list(map(int,si())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y+ 1)
        return True
    return False

ans = 0 
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            ans += 1
            
print(ans)