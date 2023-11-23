alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

for i in range (1, 10):
    print((alphabet[:2*i+1] * 2)[:i*2-1])


