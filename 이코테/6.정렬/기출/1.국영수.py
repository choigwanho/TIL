import sys
si = sys.stdin.readline

n = int(si()) # 반의 학생 수 
students = [] 
for _ in range(n):
    students.append(si().split()) # 학생의 이름, 국어 점수, 영어 점수, 수학 점수

# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 수학 점수가 감소하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])