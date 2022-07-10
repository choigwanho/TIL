# 1181 단어 정렬
"""
[입력]
입력받은 숫자만큼 반복하여 문자 입력
[알고리즘]
1. set()으로 중복제거하여 list() 저장
2. 사전순정렬 길이순으로 정렬
[출력]
반복문으로 출력
"""
def sol1181():
    n = int(input())
    words = set(input() for _ in range(n))
    wordList=list(words)

    wordList.sort()
    wordList.sort(key=len)

    for word in wordList:
        print(word)
