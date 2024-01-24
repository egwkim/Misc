import time
import random

while True:
    s = ""
    r=random.randint(1,100)
    for i in range(10):
        if (i+1)**2 >= r:
            s+=" "*(10-i)+"*"*(r-i*i-1)+"@"+"*"*(2*i+i*i-r+1)+"\n"
            r=101
        else:
            s+=" "*(10-i)+"*"*(2*i+1)+"\n"
    s+=(" "*9+"###"+"\n")*3
    print(s)
    time.sleep(0.8)
