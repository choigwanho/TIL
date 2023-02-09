import sys
si = sys.stdin.readline

bulb = {
    " ":"0000000",
    "0":"1110111",
    "1":"0010010",
    "2":"1011101",
    "3":"1011011",
    "4":"0111010",
    "5":"1101011",
    "6":"1101111",
    "7":"1110010",
    "8":"1111111",
    "9":"1111011"
}

t = int(si()) # 테스트 케이스의 수 t

for _ in range(t): # 1e3
    a, b = si().split()
    a = (5-len(a))*" " + a
    b = (5-len(b))*" " + b

    cnt = 0
    for i in range(5):
        for j in range(7):
            cnt += (bulb[a[i]][j] != bulb[b[i]][j]) # True (1), False (0) 

    # 스위치를 눌러야 하는 최소 횟수 출력
    print(cnt)