l = []

for base in range(2, 101):
    print(f"{base=}")
    count = 0
    for i in range(6):
        for j in range(10**i, 10**(i+1)-1):
            n = j
            m = j*j
            while n>0:
                if m%base != n%base:
                    break
                m //= base
                n //= base
            else:
                print(j)
                count += 1
    if count > 1:
        l.append(base)
print(l)
input()