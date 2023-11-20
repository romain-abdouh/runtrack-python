start = ord('a')
end = ord('z')

for alphabet in range(end, start - 1, - 1):
    print(chr(alphabet), end=' ')
