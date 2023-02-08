import sys
si = sys.stdin.readline

w, n = map(int,si().split()) # 배낭의 무게 w, 귀금속의 종류 n
treasure = list(list(map(int,si().split())) for _ in range(n)) # 귀금속의 무게 m, 무게당 가격 p
treasure.sort(key=lambda x:x[1], reverse=True) #가치가 높은 순으로 정렬, O(nlogn)

ans = 0
for m,p in treasure: # O(n)
    if m < w:
        ans += m*p
        w -= m
    else:
        ans += w*p
        break
print(ans)