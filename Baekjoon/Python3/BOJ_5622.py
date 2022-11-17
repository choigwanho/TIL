# 5622 다이얼
'''
1. 아이디어
- 3으로 나누어 알파벳 그룹을 나누려고 보니, 7과 9는 4글자씩 있다.
- 알파벳 리스트를 만들어서 직접 비교
2. 복잡도
- word의 길이 시간 복잡도
3. 자료구조 
- 리스트
'''
def sol5622():
    alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    word = input()

    time =0 
    for unit in alpabet_list:
        for i in unit:
            for x in word:
                if i == x:
                    time += alpabet_list.index(unit) + 3

    print(time)