'''
체격순 
같은경우 앞사람 대여가능
다른 경우 뒷학생 대여가능
전체학생 n 30
도난당한 학생 번호 30
여벌이 있는 학생 번호 30
'''
'''
def solution(n, lost, reserve):
    student = [0 for _ in range(n+1)]
    for i in lost:
        student[i] = -1
    for i in reserve:
        if student[i]==-1:
            student[i]=0
        student[i] = 1

    for i in range(1,n):
        print(student[1:])
        if student[i] == 1 and student[i-1]==-1:
            print("앞 교체 idx : ",student[i], student[i-1])
            student[i]=0
            student[i-1]=0
        if student[i] == 1 and student[i+1]==-1:
            print("뒤 교체 idx : ",student[i], student[i+1])
            student[i]=0
            student[i+1]=0
        
    ans = 0
    for s in student[1:]:
        if s>=0:
            ans+=1

    return ans
'''
'''
def solution(n, lost, reserve):
    student = list(1 for i in range(n))
    for r in reserve:
        student[r-1]=2
    for l in lost:
        if student[l-1]==2:
            student[l-1]=1
        student[l-1]=0

    for idx, s in enumerate(student):
        if s==2:
            if 0<= idx-1 <n and student[idx-1]==0:
                student[idx]=1
                student[idx-1]=1
            elif 0<= idx+1 <n and student[idx+1]==0:
                student[idx]=1
                student[idx+1]=1 
                
    return student.count(1) + student.count(2) 
'''  
def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set =  set(lost)- set(reserve)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    return n-len(lost_set)

testcase = [[5,	[2, 4],	[1, 3, 5]],
            [5,	[2, 4],	[3]],
            [3,	[3], [1]]]

for n, lost, reserve in testcase:
	print(solution(n, lost, reserve))