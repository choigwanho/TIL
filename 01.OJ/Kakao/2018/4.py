def solution(n, t, m, timetable):
    timetable = sorted([int(i[:2])*60 + int(i[3:]) for i in timetable])
    
    con = 540
    bus = 540

    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= bus:
                con = timetable.pop(0) - 1
            else:
                con = bus
        bus += t

    return f'{str(con//60).zfill(2)}:{str(con%60).zfill(2)}'

testcase = [(1,1,5,["08:00", "08:01", "08:02", "08:03"]),
            (2,10,2,["09:10", "09:09", "08:00"]),
            (1,2,1,["09:00", "09:00", "09:00", "09:00"])]

for n, t, m, timetable in testcase:
    print(solution(n, t, m, timetable))