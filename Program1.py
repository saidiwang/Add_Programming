import random
import time
import matplotlib.pyplot as plt
import numpy as np
import math


def add(n):
    if n in range(0,1001):
        a = random.randint(10**(n-1),10**n)
        b = random.randint(10**(n-1),10**n)
        c = a + b
        return c
def runningtime(n):
    Running_time = []
    for i in range(1000):
        start = time.clock()
        add(n)
        end = time.clock()
        length = end-start
        Running_time.append(length)
    Average_Running_time = sum(Running_time)/1000
    # fig1 = plt.figure()
    # plt.hist(Running_time,bins = 30,color='green',normed = False)
    # plt.title('Program_Cost_Time_Frequency Distribution')
    # plt.xlabel('Cost_Time')
    # plt.ylabel('Frequeny')
    # plt.show()
    print('%s-Running time: %s Seconds'%(n,Average_Running_time))
    return Average_Running_time

a1 = runningtime(4)
a2 = runningtime(8)
a3 = runningtime(16)
a4 = runningtime(32)
a5 = runningtime(64)
a6 = runningtime(128)
a7 = runningtime(256)
a8 = runningtime(512)
a = [float(a1)*math.exp(6),float(a2)*math.exp(6),float(a3)*math.exp(6),float(a4)*math.exp(6),float(a5)*math.exp(6),float(a6)*math.exp(6),float(a7)*math.exp(6),float(a8)*math.exp(6)]
b = [4,8,16,32,64,128,256,512]
c = np.array(b)
d = np.array(a)
plt.plot(c,d)
plt.ylabel('Average Cost Time * exp(6)')
plt.xlabel('n-digits')
plt.show()
