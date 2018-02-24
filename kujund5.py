for r in range (1, 5, 1):
    print(str(r), end=' ')
    for v in range(1, (5-r), 1):
        print(' ', end=' ')
    for v in range(1, r+1, 1):
        print('x', end=' ')
    print()