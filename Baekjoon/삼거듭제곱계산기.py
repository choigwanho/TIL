'''
삼거듭제곱계산기
'''
def solution(num):

    while num != 0:
        mod =  num%3
        num = num//3
        if mod == 2: # 2가 한번이라도 나오면 불가능
            return False
    return True

testcase = [109, 7, 36, 120, 278, 19424, 10492831]

for num in testcase:
    print(solution(num))