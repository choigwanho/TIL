# Base64 Decoder
T = int(input())
table = {s: i for i, s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}

for t in range(1,T+1):
    S = str(input())

    bit = ''.join([bin(table[s])[2:].zfill(6) for s in S])

    ans = ''.join([chr(int(bit[i:i + 8], 2)) for i in range(0, len(bit), 8)])

    print(f'#{t}',ans)

    