from collections import deque

def solution(cacheSize, cities):
    answer = 0
    l = ['']*cacheSize
    cache = deque(l, maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer


testcase =[
    [3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
    [3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]],
    [2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
    [5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
    [2,["Jeju", "Pangyo", "NewYork", "newyork"]],
    [0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]
]
for case in testcase:
    print(solution(case[0],case[1])) 