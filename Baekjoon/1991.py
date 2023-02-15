import sys 
si = sys.stdin.readline

class Node():
    def __init__(self, p, l, r):
        self.p = p
        self.l = l
        self.r = r
    
def preorder(node):
    print(node.p, end = '')
    if node.l != '.':
        preorder(tree[node.l])
    if node.r != '.':
        preorder(tree[node.r])

def inorder(node):
    if node.l != '.':
        inorder(tree[node.l])
    print(node.p, end = '')
    if node.r != '.':
        inorder(tree[node.r])

def postorder(node):
    if node.l != '.':
        postorder(tree[node.l])
    if node.r != '.':
        postorder(tree[node.r])
    print(node.p, end = '')


n = int(si()) # 이진 트리의 노드의 개수
tree = {}
for _ in range(n):
    p,l,r = map(str, si().split()) # 부모, 왼쪽 자식, 오른쪽 자식
    tree[p] = Node(p,l,r)

preorder(tree['A']) # 전위 순회
print() 
inorder(tree['A']) # 중위 순회
print()
postorder(tree['A']) # 후위 순회



