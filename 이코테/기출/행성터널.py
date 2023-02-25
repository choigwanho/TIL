import sys
si = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(si()) # 행성의 개수 (노드의 개수)
parent = [0] * (n + 1) # 부모 테이블,부모를 자기 자신으로 초기화

edges = [] # 모든 간선을 담을 리스트
ans = 0 # 최종 비용을 담을 변수

for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []

for i in range(1, n + 1):
    data = list(map(int,si().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost

print(ans) # 모든 행성을 터널로 연결하는데 필요한 최소 비용 출력