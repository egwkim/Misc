for i in range(10):
    for j in range(10**i, 10**(i+1)-1):
        if (j*j)%(10**(i+1)) == j:
            print(j)
input()