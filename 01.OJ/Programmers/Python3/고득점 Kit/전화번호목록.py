from collections import defaultdict
def solution(phone_book):
    answer = True
    temp_dict = defaultdict(int)

    for phone in phone_book:
        temp_dict[phone]

    for phone_number in phone_book:
            temp = ""
            for number in phone_number:  # 숫자 하나씩 뜯어보기
                temp += number

                if temp in temp_dict.keys() and temp != phone_number: # 딕셔너리 리스트로 바꿈
                    answer = False

    return answer