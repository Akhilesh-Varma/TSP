def patterns(n):
    for i in range(0,n+1,1):
        print('\n',end = '')
        for r in range(0,n-i):
            print(end = ' ')
        for j in range(i):
            print('*',end='')


patterns(5)