from collections import defaultdict
import sys
si = sys.stdin.readline

n,m = map(int,si().split()) # 회의실의 수 n, 예약된 회원의 수 m

room = defaultdict(list) # 회의실 이름
reservation = defaultdict(list) # 배정된 회의실 이름, 시작시간, 종료시간

for _ in range(n):
    key = si().strip()
    room[key]
    reservation[key].append(8)

for _ in range(m): 
    key, start, end = si().split()
    start, end = int(start), int(end)
    for i in range(start, end):
        reservation[key].append(i)

for key in reservation:
    reservation[key] = sorted(reservation[key])

for key in reservation:
    for i in range(len(reservation[key])):
        start = reservation[key][i]+1
        if i != len(reservation[key])-1:
            end = reservation[key][i+1]
        else:
            end = 18
        if start == end:
            continue
        if start == 9:
            start ="09"
        else:
            start = str(start)
        end = str(end)
        room[key].append(start+"-"+end)

room = sorted(room.items(), key = lambda item : item[0])
for i in range(len(room)):
    key, time = room[i][0], room[i][1]
    print(f"Room {key}:")
    if time == []:
        print("Not available")
    else:
        print(f"{len(time)} available:")
        for t in time:
            print(t)
    if i != len(room)-1:
        print("-----")