def patterns(n):
    for i in range(1,n+1):
        print("\n",end='')
        for j in range(i):
            print(""*5,'*')



patterns(5)