'''
갈색 격자의 수, 노란색 격자의 수를 입력받으면
brown = 8~ 5,000 => 오천
yellow = 1 ~ 2,000,000  => 2백만
카펫의 가로, 세로 크기를 배열에 담아서 출력
'''

def solution(brown, yellow):
    answer = []
    
    big_rectangle = brown + yellow
    small_rectangle = yellow
    
    w, h = 0, 0


    for i in range(1, small_rectangle+1):
        if small_rectangle%i == 0:
            if i > small_rectangle//i:
                break 
            h = i
            w = small_rectangle//i
            if (w+2)*(h+2) == big_rectangle:
                answer.append(w+2)
                answer.append(h+2)

    return answer

testcase = [[10, 2]
            ,[8, 1]
            ,[24, 24]]

for brown, yellow in testcase:
    print(solution(brown, yellow))