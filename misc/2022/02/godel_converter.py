from pathlib import Path


def prime_list(n):
    primes = []
    i = 2
    while len(primes) < n:
        if all(i % x for x in primes):
            primes.append(i)
        i += 1
    return primes


def convert_from_godel(n, table):
    primes = [2, 3]
    a = []
    for p in primes:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        a.append(k)
    while n != 1:
        p = primes[-1]+2
        while not all(p % x for x in primes):
            p += 2
        primes.append(p)
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        a.append(k)
    if table:
        return ''.join(table[i-1] for i in a)
    return ''.join(chr(i) for i in a)


def convert_to_godel(s, table):
    s = s.upper()
    primes = prime_list(len(s))
    n = 1
    if table:
        for i, char in enumerate(s):
            if char in table:
                n *= primes[i]**(table.index(char)+1)
            else:
                print('Error: Character not in translate table')
                return
    else:
        for i, char in enumerate(s):
            n *= primes[i]**(ord(char))
    return n


while 1:
    mode = input('(O)pen from file, (I)nt to str, (S)tr to int: ').upper()
    table = input('Use custom table?')
    if table in ['U', 'u']:
        table = 0
    elif not table:
        table = ' '+''.join(chr(i)for i in range(65, 91))
    if mode == 'O':
        path = Path(__file__).parent / "./n.txt"
        with path.open() as file:
            for line in file:
                n = int(line)
                print(convert_from_godel(n, table))
    elif mode == 'I':
        print(convert_from_godel(int(input('Input: ')), table))
    elif mode == 'S':
        print(convert_to_godel(input(), table))
    else:
        continue
    break
