def rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('+' + '-' * (width - 2) + '+')
        else:
            hashes = '#' * (height - i -1)
            spaces = ' '
            line = '|' + hashes + spaces + '#'*i + '|'
            print(line)


rectangle(12, 10)