def solution(cap, n, deliveries, pickups):
    answer = -1
     

    for i in range(n):

        cap +=caps[i]
        

    print(caps)
    return
    
    
    



testcase= [
    (4,5, [1,0,3,1,2], [0,3,0,4,0]),
    (2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
]
for cap, n, deliveries, pickups in testcase:
    print(solution(cap, n, deliveries, pickups))