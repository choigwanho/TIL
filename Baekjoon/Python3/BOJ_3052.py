# 3052 나머지
def sol3052():
    mods=[]

    for _ in range(10):
        mods.append(int(input())%42)

    print(len(list(set(mods))))