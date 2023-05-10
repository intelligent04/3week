t = int(input())
for _ in range(t):
    dec_output=0
    bits = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    dec_input = int(input())
    dec_bi = []
    while not dec_input<= 1:
        dec_bi.insert(0,dec_input%2)
        dec_input = dec_input//2
    dec_bi.insert(0,dec_input)
    for __ in range(len(dec_bi)):
        bits.pop()
    bits.extend(dec_bi)
    if sum(dec_bi)%2 == 1 and bits[0]==0:
        bits[0] = 1
    elif sum(dec_bi)%2 == 1 and bits[0]==1:
        bits[0] = 0
    bits.reverse()
    for i in range(32):
        dec_output = dec_output + bits[i]*(2**i)
    print(dec_output)

