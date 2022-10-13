'''
LCS 
최대 공통 부분 수열 (Longest Common Subsequence) 
'''
def solution(A,B):
    LCS = [[0]*(len(A)) for _ in range(len(B))]

    for i in range(len(B)):
        for j in range(len(A)):
            if B[i] == A[j]:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1], LCS[i - 1][j - 1] + 1)
    
    for i in range(len(B)):
        print(LCS[i])

testcase = [['melon', 'watermelon']]
# ['back','bag'],
# ['apple','application'],
# ['isiteasy','itiseasy'],
# ['alogrithmjobs','aldentespaghetti'],
# ['editdistanceproblem','dijkstraalgorithm']]

for A,B in testcase:
    print(solution(A,B))