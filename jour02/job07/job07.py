alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

for i in range (1, len(alphabet)):
    subset = alphabet[:2*i+1]
    repeated_subset = (subset * 2)[:i*2-1]
    print(repeated_subset)


