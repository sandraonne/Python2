for r in range (1, 5, 1):
    print(str(r), end=' ')
    for v in range(1, 5, 1):
        if(v == (5-r)):
            break
        print(' ', end=' ')
    for v in range(1, 5, 1):
        if(v == (r+1)):
            break
        print('x', end=' ')
    for v in range(1, 5, 1):
        if (v==r):
            break
        print('0', end=' ')
    print()