import sys 
si = sys.stdin.readline

n = int(si()) # 주어진 돈
cnt = 0

coin_list = [500, 100, 50, 10] # 화폐단위

for coin in coin_list:
    cnt += n // cnt # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= coin

print(cnt)