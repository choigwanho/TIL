import sys
si = sys.stdin.readline

n,m = map(int,si().split()) # 포켓몬의 개수 n, 맞춰야 하는 문제의 개수 m
name_dict = dict()
num_dict = dict()
for num in range(1, n+1):
    name = si().strip()
    name_dict[name] = num
    num_dict[str(num)] = name

for _ in range(m):
    key = si().strip() 
    if key in name_dict.keys():
        print(name_dict[key])
    elif key in num_dict.keys():
        print(num_dict[key])
