# 10816번 숫자 카드 2

'''
정보를 저장해야 할 카드는 50만개이고, 조회할 카드의 개수도 50만 개이므로 이중 for loop를 피해야한다.
따라서, <카드번호> : <카드의 개수> 쌍으로 저장하기 위해 딕셔너리 사용해서 카드를 입력 받으면서 카드의 개수를 저장하고, 궁금한 카드에 대해서 값만 조회한다. 
시간복잡도는 딕셔너리에 저장하는 횟수 n과 조회하는 횟수 m으로 상수 시간 복잡도 50만으로 해결이 가능하다.
'''

from collections import defaultdict
import sys
si = sys.stdin.readline

cardCntDict = defaultdict(int) # 숫자의 개수를 저장할 딕셔너리

n = int(si()) # 숫자 카드 n개
for card in list(map(int, si().split())): # n개의 숫자 카드에 적혀있는 정수 카운팅
    cardCntDict[card] += 1

m = int(si()) # 정수 m개
for target in list(map(int, si().split())): # 구해야 할 m개의 정수의 개수를 조회해서 출력
    print(cardCntDict[target], end=" ")